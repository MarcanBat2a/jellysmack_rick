from fastapi import APIRouter
from app.core.character_manager import CharacterManager
from app.adapters.character_table import AdapterCharacter
from app.adapters.postgres.client import Database

# Cest de la merde à voir pour eviter la redondance des imports dans main
database = Database()
adapter = AdapterCharacter(database)
character_manager = CharacterManager(adapter)
# Cest de la merde à voir pour eviter la redondance des imports


router = APIRouter()

@router.get("/characters")
def read_characters(limit:int=0, page:int=0):
    return character_manager.get_all(limit, page), 200

