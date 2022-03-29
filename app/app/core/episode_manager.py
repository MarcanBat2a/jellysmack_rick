class EpisodeManager:
    def __init__(self, adapter) -> None:
        self.adapter = adapter
    

    def get_all(self):
        list_episodes = []
        for episode in self.adapter.get_all():
            list_episodes.append(episode.to_dict())
        
        return list_episodes
    

    def get_by_id(self, id):
        return self.adapter.get_by_id(id).to_dict()
