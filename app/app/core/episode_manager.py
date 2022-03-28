class EpisodeManager:
    def __init__(self, adapter) -> None:
        self.adapter = adapter
    
    def get_all(self):
        list_episodes = []
        for episode in self.adapter.get_all():
            list_episodes.append(episode.to_dict())
        
        return list_episodes
    
