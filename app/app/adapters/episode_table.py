from app.adapters.base_table import AdapterBase
from app.model.episode import Episode


class AdapterEpisode(AdapterBase):
    def __init__(self) -> None:
        super().__init__(item="episodes", model=Episode)
    

    def get_by_id_all_characters(self, id:int)->list:
        query = "SELECT id_character FROM characters_episodes WHERE id_episode = %s"
        self.database.cur.execute(query, (id,))
        list_id_characters = []
        for dict_characters in self.database.cur.fetchall():
            list_id_characters.append(dict_characters.get('id_character'))
        return list_id_characters
         