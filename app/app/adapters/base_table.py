from abc import ABC
import json


class AdapterBase(ABC):
    COLUMNS = []

    OPERATORS = [
        "=",
        ">",
        "<",
        ">=",
        "<=",
        "<>", 	
        "IN",	
        "BETWEEN",	
        "LIKE",
        "IS NULL",
        "NOT"]


    def __init__(self, database, item:str, model) -> None:
        self.database = database
        self.item = item
        self.model = model
    

    def parse_filter(self, list_all_filters:str):
        list_all_filters = json.loads(list_all_filters)
        list_filters = []
        last_id_filters = -1
        query = " WHERE"
        for i_filters in range(len(list_all_filters)):
            for key, filters in list_all_filters[i_filters].items():
                for filter in filters:  
                    if filter.get("operator").upper() in self.OPERATORS and key.lower() in self.COLUMNS:
                        if last_id_filters == i_filters:
                            query += ' AND '+ key + ' ' + filter.get("operator") + ' %s'
                            
                        elif last_id_filters == -1:
                            query += ' '+key+' '+ filter.get("operator")+' %s'
                        else:
                            query += ' OR '+key+' '+ filter.get("operator")+' %s'
                        last_id_filters = i_filters

                        if type(filter.get("value")) is list:
                            filter["value"] = tuple(filter.get("value"))
                        list_filters.append(filter.get("value"))

        return query, list_filters
        

    def pagination(self, limit:int, num_page:int):
        placeHolder_params = []
        offset = limit*(num_page-1)
        query = " LIMIT %s OFFSET %s"
        placeHolder_params.append(limit)
        placeHolder_params.append(offset)
        return query, placeHolder_params


    def get_number_rows(self, filter:list=[]):
        self.database.cur.execute(query, placeHolder_params)
        character_records = self.database.cur.fetchall()


    def get_all(self):
        query = "SELECT * FROM {}".format(self.item)
        self.database.cur.execute(query)
        item_records = self.database.cur.fetchall()
        list_items = []
        for ite in item_records:
            list_items.append(self.model.generate(ite))
        return list_items
    