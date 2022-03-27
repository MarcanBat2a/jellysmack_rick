from typing import Optional
from fastapi import FastAPI
import os
from app.adapters.postgres import client
from app.data.import_data import import_data_to_database


db = client.database()
print("coucou")
app = FastAPI()


@app.get("/")
def read_root():
    import_data_to_database(db)
    return 'lalaalalala', 200


if __name__== "__main__":
    print("juste pour voir")
    #import_data_to_database(db)
