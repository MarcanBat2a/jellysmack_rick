from app.model.character import Character
from app.adapters.base_table import AdapterBase
from math import ceil

class AdapterCharacter(AdapterBase):
    COLUMNS = ["id", "name", "status", "species", "type", "gender"]
    def __init__(self, database) -> None:
        super().__init__(database = database, item="characters", model=Character) 


    def get_all_with_filter_pagination(self, limit: int, num_page:int, list_all_filters:str):
        query = "SELECT * FROM characters"
        values_filer = []
        placeHolder_params_pagine = []
        total_page = 1
        if len(list_all_filters) > 0:
            query_filter, values_filer = self.parse_filter(list_all_filters)
            query += query_filter
        if limit != 0 and num_page != 0:
            self.database.cur.execute("SELECT COUNT(*) FROM characters", values_filer)
            total_rows = self.database.cur.fetchall()[0].get("count")
            total_page = ceil(total_rows/limit)
            query_pagine, placeHolder_params_pagine = self.pagination(limit, num_page)
            query += query_pagine

     
        placeHolder_params = values_filer + placeHolder_params_pagine

        self.database.cur.execute(query, placeHolder_params)
        character_records = self.database.cur.fetchall()
        
        list_characters = []
        for character in character_records:
            list_characters.append(self.model.generate(character))

        return list_characters, total_page
