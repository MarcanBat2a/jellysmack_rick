from app.adapters.character_table import AdapterCharacter
from app.core.character_manager import CharacterManager
from fastapi import APIRouter

adapter = AdapterCharacter()
character_manager = CharacterManager(adapter)

router = APIRouter()

@router.get("/")
def read_characters(limit:int=0, page:int=0, search:str=""):
    if (limit>0 and page>0) or search != "":
        return character_manager.get_all_with_filter_pagination(limit, page, search)
    return character_manager.get_all()
