import re
import sys
sys.path.append('../')
from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import models as _models
import schemas.transactions as _schemas
import services.transactions as _services
import services.users as _services_users
import utils as _utils
from auth import AuthHandler


auth_handler = AuthHandler()


transaction_router=_fastapi.APIRouter(
    prefix="/transaction",
    tags=['transaction']
)

# GET
@transaction_router.get("/get-all-transactions", response_model=List[_schemas.Transaction])
async def get_all_transactions(db: _orm.Session = _fastapi.Depends(_utils.get_db), token=_fastapi.Depends(auth_handler.auth_wrapper)):
    return await _services.get_all_transactions(db=db)

@transaction_router.get("/get-user-transactions/{user_id}", response_model=List[_schemas.Transaction])
async def get_user_transactions(user_id: int, db: _orm.Session = _fastapi.Depends(_utils.get_db), token=_fastapi.Depends(auth_handler.auth_wrapper)):
    transaction_in = await _services.get_transactions_in(user_id=user_id, db=db)
    transaction_out = await _services.get_transactions_out(user_id=user_id, db=db)
    return transaction_in + transaction_out

# CREATE
@transaction_router.post('/create_transaction', status_code=201)
async def create_transactions(transactions_details: _schemas.UserTransaction, db: _orm.Session = _fastapi.Depends(_utils.get_db), token=_fastapi.Depends(auth_handler.auth_wrapper)):
    transactions = await _services.get_all_transactions(db=db)
    sender = await _services_users.get_user_by_id(user_id=transactions_details.sender_id, db=db)
    receiver = await _services_users.get_user_by_username(username=transactions_details.receiver_username, db=db)
    if(receiver is None or receiver.status == 0):
        raise _fastapi.HTTPException(status_code=401, detail='Penerima tidak valid!')
    if (sender.balance - transactions_details.nominal < 0):
        raise _fastapi.HTTPException(status_code=401, detail='Saldo tidak cukup!')
    transaction = { 'transaction_id': len(transactions), 'sender_id': sender.user_id, 'receiver_id': receiver.user_id, 'nominal': transactions_details.nominal}
    await _services.create_transaction(transaction=transaction, db=db)
    await _services_users.add_balance_user(balance=transactions_details.nominal, user=receiver, db=db)
    await _services_users.minus_balance_user(balance=transactions_details.nominal, user=sender, db=db)
    return "Berhasil melakukan transaksi!"