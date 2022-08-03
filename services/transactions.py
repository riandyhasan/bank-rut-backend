import sys
sys.path.append('../')

from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas.transactions as _transactions 

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

# GET
async def get_all_transactions(db: "Session") -> List[_transactions.Transaction]:
    transactions = db.query(_models.Transactions).all()
    return list(map(_transactions.Transaction.from_orm, transactions))

async def get_transactions_out(user_id: int, db: "Session") -> List[_transactions.Transaction]:
    user_transactions = db.query(_models.Transactions).filter(_models.Transactions.sender_id == user_id).all()
    return user_transactions

async def get_transactions_in(user_id: int, db: "Session") -> List[_transactions.Transaction]:
    user_transactions = db.query(_models.Transactions).filter(_models.Transactions.receiver_id == user_id).all()
    return user_transactions

# CREATE
async def create_transaction(
    transaction: _transactions.CreateTransaction, db: "Session"
) -> _transactions.Transaction:
    transaction = _models.Transactions(**transaction)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return _transactions.Transaction.from_orm(transaction)