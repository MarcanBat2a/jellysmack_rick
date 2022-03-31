from app.model.character import Character
from app.adapters.item_table import AdapterItem
import json
class AdapterCharacter(AdapterItem):
    def __init__(self, database) -> None:
        super().__init__(database = database, item="characters", model=Character) 


    def get_all(self, limit: int, num_page:int, list_all_filters:str):
        placeHolder_params = []
        query = "SELECT * FROM characters"
    
        if len(list_all_filters) > 0:
            list_all_filters = json.loads(list_all_filters)
 
            list_placeHolders = []
            list_filters = []
            last_id_filters = -1

            for i_filters in range(len(list_all_filters)):
                
                for key, filters in list_all_filters[i_filters].items(): 
                    for filter in filters:       
                        if last_id_filters == i_filters:
                            list_placeHolders.append(' AND {} {} {}')
                           
                        elif last_id_filters == -1:
                            list_placeHolders.append('{} {} {}')
                        else:
                            list_placeHolders.append(' OR {} {} {}')
                        last_id_filters = i_filters
                        
                        list_filters.append({
                        "column":key,
                        "operator":filter.get("operator"),
                        "value": filter.get("value")})

            
            query_filter = "{}"
            for i in range(len(list_placeHolders)):
                query_filter = query_filter.format(list_placeHolders[i])
                query_filter = query_filter.format(list_filters[i].get("column"), list_filters[i].get("operator"), list_filters[i].get("value"))
                if i < len(list_placeHolders)-1:
                    query_filter += "{}"
            
            print(query_filter)
            query += " WHERE %s"
            placeHolder_params.append(query_filter)


        if limit != 0 and num_page != 0:
            offset = limit*(num_page-1)
            query += " LIMIT %s OFFSET %s"
            placeHolder_params.append(limit)
            placeHolder_params.append(offset)

        self.database.cur.execute(query, placeHolder_params)

        character_records = self.database.cur.fetchall()
        list_characters = []
        for character in character_records:
            list_characters.append(self.model.generate(character))
        return list_characters