class Episode():
    def __init__(self, id_episode:int, name:str, air_date:str, episode:str, list_character:list=[]) -> None:
        self.id_episode = id_episode
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.list_character = list_character


    @staticmethod
    def generate(episode:dict):
        return Episode(
            id_episode = episode.get('id'),
            name = episode.get('name'),
            air_date = episode.get('air_date'),
            episode = episode.get('episode')
        )


    def to_dict(self):
        return {"id_episode": self.id_episode,
            "name": self.name,
            "air_date": self.air_date,
            "episode": self.episode}
