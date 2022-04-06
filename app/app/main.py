from fastapi import FastAPI

from app.adapters.postgres.client import Database

from app.api.api_v1.api import api_router
from app.data.import_data import import_data_to_database

db = Database()

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return 'Hello Smack'


@app.put("/populate-db")
def populate_db():
    import_data_to_database(db)
    return 'Hello Smack'
