from app.model.character import Character
from app.adapters.item_table import AdapterItem

class AdapterCharacter(AdapterItem):
    def __init__(self, database) -> None:
        super().__init__(database = database, item="characters", model=Character) 


    def get_all(self, limit:int, num_page:int):
        if limit != 0 and num_page != 0:
            offset = limit*(num_page-1)
            query = "SELECT * FROM characters LIMIT %s OFFSET %s"
            self.database.cur.execute(query, (limit, offset))
        else:
            query = "SELECT * FROM characters"
            self.database.cur.execute(query)
        character_records = self.database.cur.fetchall()
        list_characters = []
        for character in character_records:
            list_characters.append(self.model.generate(character))
        return list_characters