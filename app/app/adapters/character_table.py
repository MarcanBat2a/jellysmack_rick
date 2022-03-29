from app.model.character import Character

class AdapterCharacter:
    def __init__(self, database) -> None:
        self.database = database
    
    def get_all(self):
        query = "SELECT * FROM characters"
        self.database.cur.execute(query)
        character_records = self.database.cur.fetchall()
        list_characters = []

        for character in character_records:
            list_characters.append(Character.generate(character))
        return list_characters