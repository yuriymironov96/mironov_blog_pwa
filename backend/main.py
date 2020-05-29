from fastapi import FastAPI

from apps.core.database import SessionLocal, engine, Base
from apps.auth.models import Base

app = FastAPI()


@app.get('/')
async def read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    return {'item_id': item_id, 'q': q}