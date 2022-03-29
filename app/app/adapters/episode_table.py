from app.model.episode import Episode

class AdapterEpisode:
    def __init__(self, database) -> None:
        self.database = database
    
    
    def get_all(self):
        query = "SELECT * FROM episodes"
        self.database.cur.execute(query)
        episode_records = self.database.cur.fetchall()
        list_episodes = []

        for episode in episode_records:
            list_episodes.append(Episode.generate(episode))
        return list_episodes
    

    def get_by_id(self, id):
        query = "SELECT * FROM episodes WHERE %s"
        self.database.cur.execute(query, id)
        return Episode.generate(self.database.cur.fetchall())