import os
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from databases import Database

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

authors = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("firstname", String(50)),
    Column("surname", String(50)),
    Column("year_of_birth", Integer),
    Column("year_of_death", Integer),
    Column("nationality", String(50)),
)

database = Database(DATABASE_URI)
