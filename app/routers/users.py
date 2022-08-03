import sys
sys.path.append('../')
from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import models as _models
import schemas.users as _schemas
import services.users as _services
import utils as _utils
from auth import AuthHandler


auth_handler = AuthHandler()

user_router=_fastapi.APIRouter(
    prefix="/user",
    tags=['user']
)

# GET
@user_router.get("/get-all-users", response_model=List[_schemas.UserData])
async def get_all_users(db: _orm.Session = _fastapi.Depends(_utils.get_db), token=_fastapi.Depends(auth_handler.auth_wrapper)):
    return await _services.get_all_users(db=db)

@user_router.get("/get-user/{user_id}", response_model=_schemas.UserData)
async def get_user(user_id: int, token=_fastapi.Depends(auth_handler.auth_wrapper), db: _orm.Session = _fastapi.Depends(_utils.get_db)):
    user = await _services.get_user_by_id(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User tidak ada!")
    return user

# CREATE
@user_router.post('/register', status_code=201)
async def register(user_details: _schemas.UserRegistration, db: _orm.Session = _fastapi.Depends(_utils.get_db)):
    users = await _services.get_all_users(db=db)
    if any(x.username == user_details.username for x in users):
        raise _fastapi.HTTPException(status_code=400, detail='Username sudah ada')
    password = user_details.password
    hashed_password = auth_handler.get_password_hash(user_details.password)
    user_details.password = hashed_password
    created_users = { 'user_id': len(users), 'balance': 0, 'role': 0, 'status': 0 }
    created_users.update(user_details)
    await _services.create_user(user=created_users, db=db)
    auth_details = {'username': user_details.username, 'password': password }
    structured_auth = _schemas.UserLogin(**auth_details)
    auth = await login(user_details=structured_auth, db=db)
    return { 'token': auth['token'], 'data': auth['data'], 'message': "Berhasil register!" }

# UPDATE
@user_router.put("/verify-user/{user_id}")
async def verify_user(user_id: int, db: _orm.Session = _fastapi.Depends(_utils.get_db), token=_fastapi.Depends(auth_handler.auth_wrapper)):
    user = await _services.get_user_by_id(user_id=user_id, db=db)
    if user is None:
        raise _fastapi.HTTPException(status_code=404, detail="User tidak ada!")
    await _services.verify_user(user, db=db)
    return 'Berhasil verifikasi user!'

# AUTH
@user_router.post('/login')
async def login(user_details: _schemas.UserLogin, db: _orm.Session = _fastapi.Depends(_utils.get_db)):
    user = None
    user = await _services.get_user_by_username(username=user_details.username, db=db)
    
    if (user is None) or (not auth_handler.verify_password(user_details.password, user.password)):
        raise _fastapi.HTTPException(status_code=401, detail='Username atau password salah')
    token = auth_handler.encode_token(user.username)
    userData = await _services.get_user_by_id(user_id=user.user_id, db=db)
    return { 'token': token, 'data': userData, 'message': "Berhasil login!" }