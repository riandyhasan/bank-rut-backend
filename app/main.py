import uvicorn
import fastapi as _fastapi
from fastapi.middleware.cors import CORSMiddleware
import sys
sys.path.append('./')
from routers.users import user_router
from routers.requests import request_router
from routers.transactions import transaction_router

app = _fastapi.FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "https://bank-rut-frontend.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(request_router)
app.include_router(transaction_router)