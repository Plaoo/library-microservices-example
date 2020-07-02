import os
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, ARRAY
from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")


engine = create_engine(DATABASE_URI)
metadata = MetaData()


books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("year", Integer),
    Column("genres", ARRAY(String)),
    Column("authors_id", ARRAY(Integer)),
)

database = Database(DATABASE_URI)
