import sys
sys.path.append('../')

from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas.requests as _requests 

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

# GET
async def get_all_requests(db: "Session") -> List[_requests.Request]:
    requests = db.query(_models.Requests).all()
    return list(map(_requests.Request.from_orm, requests))

async def get_user_requests(user_id: int, db: "Session") -> List[_requests.Request]:
    user_requests = db.query(_models.Requests).filter(_models.Requests.user_id == user_id).all()
    return user_requests

async def get_request_by_id(request_id: int, db: "Session") -> _requests.Request:
    request = db.query(_models.Requests).filter(_models.Requests.request_id == request_id).first()
    return request

# CREATE
async def create_request(
    request: _requests.CreateRequest, db: "Session"
) -> _requests.Request:
    request = _models.Requests(**request)
    db.add(request)
    db.commit()
    db.refresh(request)
    return _requests.Request.from_orm(request)

# UPDATE
async def decline_request(
    request: _models.Requests, db: "Session"
) -> _requests.Request:
    # request.user_id = request_data.user_id
    # request.nominal = request_data.nominal
    # request.jenis = request_data.jenis
    request.status = 1
    db.commit()
    db.refresh(request)
    return _requests.Request.from_orm(request)

async def approve_request(
    request: _models.Requests, db: "Session"
) -> _requests.Request:
    # request.user_id = request_data.user_id
    # request.nominal = request_data.nominal
    # request.jenis = request_data.jenis
    request.status = 2
    db.commit()
    db.refresh(request)
    return _requests.Request.from_orm(request)