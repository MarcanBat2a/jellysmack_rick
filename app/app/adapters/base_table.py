from app.adapters.postgres.client import Database
import json
from abc import ABC


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


    def __init__(self, item:str, model) -> None:
        self.database = Database()
        self.item = item
        self.model = model


    def parse_filter(self, list_all_filters:str):
        list_all_filters = json.loads(list_all_filters)
        list_filters = []
        last_id_filters = -1
        query = " WHERE"
        for i_filters, value in enumerate(list_all_filters):
            for key, filters in value.items():
                for a_filter in filters:
                    if a_filter.get("operator").upper() in self.OPERATORS and key.lower() in self.COLUMNS:
                        if last_id_filters == i_filters:
                            query += ' AND '+ key + ' ' + a_filter.get("operator") + ' %s'
                        elif last_id_filters == -1:
                            query += ' '+key+' '+ a_filter.get("operator")+' %s'
                        else:
                            query += ' OR '+key+' '+ a_filter.get("operator")+' %s'
                        last_id_filters = i_filters

                        if isinstance(a_filter.get("value"), list):
                            a_filter["value"] = tuple(a_filter.get("value"))
                        list_filters.append(a_filter.get("value"))

        return query, list_filters


    def pagination(self, limit:int, num_page:int):
        placeholder_params = []
        offset = limit*(num_page-1)
        query = " LIMIT %s OFFSET %s"
        placeholder_params.append(limit)
        placeholder_params.append(offset)
        return query, placeholder_params


    def get_all(self):
        query = "SELECT * FROM {}".format(self.item)
        self.database.cur.execute(query)
        item_records = self.database.cur.fetchall()
        list_items = []
        for ite in item_records:
            list_items.append(self.model.generate(ite))
        return list_items
    