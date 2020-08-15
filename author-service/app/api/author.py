from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import AuthorOut, AuthorIn, AuthorUpdate
from app.api import db_manager
import json
import logging
from fastapi.encoders import jsonable_encoder
log = logging.getLogger(__name__)
from aiocache import cached, Cache
from aiocache.serializers import JsonSerializer, PickleSerializer

authors = APIRouter()


@authors.get("/", response_model=List[AuthorOut])
@cached(
    ttl=10,
    cache=Cache.REDIS,
    endpoint="192.168.1.54",
    serializer=JsonSerializer(),
    port=6379,
    namespace="main",
    #key="key",
)
async def get_authors():
    return jsonable_encoder(await db_manager.get_all_authors())


@authors.post("/", response_model=AuthorOut, status_code=201)
async def create_author(payload: AuthorIn):
    author_id = await db_manager.add_author(payload)
    response = {"id": author_id, **payload.dict()}
    return response


@authors.get("/{id}", response_model=AuthorOut)
@cached(ttl=100)
async def get_author(id: int):
    author = await db_manager.get_author(id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not Found")
    return author


@authors.put("/{id}", response_model=AuthorOut)
async def update_author(id: int, payload: AuthorUpdate):
    author = await db_manager.get_author(id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not Found")
    update_data = payload.dict(exclude_unset=True)
    author_id_db = AuthorIn(**author)

    update_author = author_id_db.copy(update=update_data)
    update = await db_manager.update_author(id, update_author)
    return await get_author(id)


@authors.delete("/{id}", response_model=None)
async def delete_author(id: int):
    author = await db_manager.get_author(id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return await db_manager.delete_author(id)
