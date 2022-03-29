class CharacterManager:
    def __init__(self, adapter) -> None:
        self.adapter = adapter
    
    def get_all(self):
        list_characters = []
        for character in self.adapter.get_all():
            list_characters.append(character.to_dict())
        
        return list_characters