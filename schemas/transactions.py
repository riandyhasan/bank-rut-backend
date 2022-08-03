import pydantic as _pydantic

class BaseTransaction(_pydantic.BaseModel):
    sender_id: int
    receiver_id: int
    nominal: int

class Transaction(BaseTransaction):
    transaction_id: int

    class Config:
        orm_mode = True


class CreateTransaction(BaseTransaction):
    pass

class UserTransaction(_pydantic.BaseModel):
    sender_id: int
    receiver_username: str
    nominal: int