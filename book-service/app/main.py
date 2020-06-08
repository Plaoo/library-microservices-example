from fastapi import FastAPI
from app.api.book import books
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/book/openapi.json", docs_url="/api/v1/book/docs")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(books, prefix='/api/v1/book', tags=['books'])
