class CharacterManager:
    def __init__(self, adapter) -> None:
        self.adapter = adapter
    
    
    def get_all(self, limit, num_page, filter):
        list_characters = []
        for character in self.adapter.get_all(limit, num_page, filter):
            list_characters.append(character.to_dict())
        
        return list_characters

    
    def get_by_id(self, id):
        return self.adapter.get_by_id(id).to_dict()