from app.model.character import Character
from app.adapters.item_table import AdapterItem

class AdapterCharacter(AdapterItem):
    def __init__(self, database) -> None:
        super().__init__(database = database, item="characters", model=Character) 
