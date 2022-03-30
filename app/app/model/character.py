class Character():
    def __init__(self, id:int, name:str, status:str, species:str, type:str, gender:str, list_episodes=[]) -> None:
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.list_episodes = list_episodes
        
    
    @staticmethod
    def generate(character:dict):
        return Character(
            id = character.get('id'),
            name = character.get('name'),
            status = character.get('status'),
            species = character.get('species'),
            type = character.get('type'),
            gender = character.get('gender')
        )

    
    def to_dict(self):
        return {"id": self.id,
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "type": self.type,
            "gender": self.gender}