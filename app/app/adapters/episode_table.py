from app.model.episode import Episode
from app.adapters.base_table import AdapterBase

class AdapterEpisode(AdapterBase):
    def __init__(self, database) -> None:
        super().__init__(database = database, item="episodes", model=Episode)
    

    def get_by_id_all_characters(self, id):
        query = "SELECT id_character FROM characters_episodes WHERE id_episode = {}".format(id)
        self.database.cur.execute(query)
        list_id_characters = []
        for dict_characters in self.database.cur.fetchall():
            list_id_characters.append(dict_characters.get('id_character'))
        return list_id_characters
         
    
