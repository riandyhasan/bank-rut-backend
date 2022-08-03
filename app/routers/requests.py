import re
import sys
sys.path.append('../')
from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import models as _models
import schemas.requests as _schemas
import services.requests as _services
import services.users as _services_users
import utils as _utils
from auth import AuthHandler


auth_handler = AuthHandler()


request_router=_fastapi.APIRouter(
    prefix="/request",
    tags=['request']
)

# GET
@request_router.get("/get-all-requests", response_model=List[_schemas.Request])
async def get_all_users(db: _orm.Session = _fastapi.Depends(_utils.get_db), token=_fastapi.Depends(auth_handler.auth_wrapper)):
    return await _services.get_all_requests(db=db)

@request_router.get("/get-user-request/{user_id}", response_model=List[_schemas.Request])
async def get_user_requests(user_id: int, db: _orm.Session = _fastapi.Depends(_utils.get_db), token=_fastapi.Depends(auth_handler.auth_wrapper)):
    requests = await _services.get_user_requests(user_id=user_id, db=db)
    return requests

# CREATE
@request_router.post('/create_request', status_code=201)
async def create_request(request_details: _schemas.BaseRequest, db: _orm.Session = _fastapi.Depends(_utils.get_db), token=_fastapi.Depends(auth_handler.auth_wrapper)):
    requests = await _services.get_all_requests(db=db)
    requested = { 'request_id': len(requests)}
    requested.update(request_details)
    await _services.create_request(request=requested, db=db)
    return "Berhasil membuat request!"

# UPDATE
@request_router.get("/approve-request/{request_id}", status_code=201)
async def approve_request(request_id: int, db: _orm.Session = _fastapi.Depends(_utils.get_db), token=_fastapi.Depends(auth_handler.auth_wrapper)):
    request = await _services.get_request_by_id(request_id=request_id, db=db)
    if request is None:
        raise _fastapi.HTTPException(status_code=404, detail="Request tidak ada!")
    await _services.approve_request(request=request, db=db)
    user = await _services_users.get_user_by_id(user_id=request.user_id, db=db)
    if(request.jenis == 0):
        await _services_users.add_balance_user(balance=request.nominal, user=user, db=db)
    elif(request.jenis == 1):
         await _services_users.minus_balance_user(balance=request.nominal, user=user, db=db)
    return "Berhasil menerima request"

@request_router.get("/decline-request/{request_id}", status_code=201)
async def decline_request(request_id: int, db: _orm.Session = _fastapi.Depends(_utils.get_db), token=_fastapi.Depends(auth_handler.auth_wrapper)):
    request = await _services.get_request_by_id(request_id=request_id, db=db)
    if request is None:
        raise _fastapi.HTTPException(status_code=404, detail="Request tidak ada!")
    await _services.decline_request(request=request, db=db)
    return "Berhasil menolak request"