import pydantic as _pydantic

class BaseRequest(_pydantic.BaseModel):
    user_id: int
    nominal: int
    jenis: int
    status: int

class Request(BaseRequest):
    request_id: int

    class Config:
        orm_mode = True


class CreateRequest(BaseRequest):
    pass