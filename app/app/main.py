import os
from typing import Optional

from fastapi import FastAPI

from app.adapters.postgres.client import Database
from app.api import episode

from app.data.import_data import import_data_to_database

db = Database()

app = FastAPI()

app.include_router(episode.router)


@app.get("/")
def read_root():
    return 'Hello Smack'


@app.get("/populate-db")
def populate_db():
    import_data_to_database(db)
    return 'Hello Smack'


if __name__== "__main__":
    print("juste pour voir")
    #import_data_to_database(db)
