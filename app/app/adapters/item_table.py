from abc import ABC

class AdapterItem(ABC):
    def __init__(self, database, item, model) -> None:
        self.database = database
        self.item = item
        self.model = model
    
    
    def get_all(self):
        query = "SELECT * FROM {}".format(self.item)
        self.database.cur.execute(query)
        item_records = self.database.cur.fetchall()
        list_items = []
        
        for ite in item_records:
            list_items.append(self.model.generate(ite))
        return list_items
    

    def get_by_id(self, id):
        query = "SELECT * FROM %s WHERE %s"
        self.database.cur.execute(query, (self.item, id))
        return self.model.generate(self.database.cur.fetchall())