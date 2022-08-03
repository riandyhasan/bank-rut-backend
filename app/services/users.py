import sys
sys.path.append('../')

from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas.users as _users 

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

# GET
async def get_all_users(db: "Session") -> List[_users.UserData]:
    users = db.query(_models.Users).all()
    return list(map(_users.UserData.from_orm, users))

async def get_user_by_id(user_id: int, db: "Session") -> _users.UserData:
    user = db.query(_models.Users).filter(_models.Users.user_id == user_id).first()
    return user

async def get_user_by_username(username: str, db: "Session") -> _users.User:
    user = db.query(_models.Users).filter(_models.Users.username == username).first()
    return user

# CREATE
async def create_user(
    user: _users.CreateUser, db: "Session"
) -> _users.User:
    user = _models.Users(**user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return _users.User.from_orm(user)

# UPDATE
async def verify_user(
    user: _users.CreateUser, db: "Session"
) -> _users.User:
    user.status = 1
    db.commit()
    db.refresh(user)
    return _users.User.from_orm(user)

async def add_balance_user(
    balance: int, user: _users.UserData, db: "Session"
) -> _users.User:
    user.balance += balance
    db.commit()
    db.refresh(user)
    return _users.User.from_orm(user)

async def minus_balance_user(
    balance: int, user: _users.UserData, db: "Session"
) -> _users.User:
    user.balance -= balance
    db.commit()
    db.refresh(user)
    return _users.User.from_orm(user)