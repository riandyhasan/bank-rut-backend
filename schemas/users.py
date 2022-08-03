import pydantic as _pydantic

class BaseUser(_pydantic.BaseModel):
    full_name: str
    username: str
    password: str
    ktp: str
    balance: int
    status: int
    role: int

class User(BaseUser):
    user_id: int

    class Config:
        orm_mode = True


class CreateUser(BaseUser):
    pass

class UserData(_pydantic.BaseModel):
    user_id: int
    full_name: str
    username: str
    ktp: str
    balance: int
    status: int
    role: int

    class Config:
        orm_mode = True

class UserLogin(_pydantic.BaseModel):
    username: str
    password: str

class UserRegistration(_pydantic.BaseModel):
    full_name: str
    username: str
    password: str
    ktp: str

    class Config:
        orm_mode = True