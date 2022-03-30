class Episode():
    def __init__(self, id:int, name:str, air_date:str, episode:str, list_character=[]) -> None:
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.list_character = list_character
    
    
    @staticmethod
    def generate(episode:dict):
        return Episode(
            id = episode.get('id'),
            name = episode.get('name'),
            air_date = episode.get('air_date'),
            episode = episode.get('episode')
        )
    
    
    def to_dict(self):
        return {"id": self.id,
            "name": self.name,
            "air_date": self.air_date,
            "episode": self.episode}