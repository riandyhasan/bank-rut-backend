import uvicorn
import fastapi as _fastapi
import sys
sys.path.append('./')
from routers.users import user_router
from routers.requests import request_router
from routers.transactions import transaction_router

app = _fastapi.FastAPI()

app.include_router(user_router)
app.include_router(request_router)
app.include_router(transaction_router)