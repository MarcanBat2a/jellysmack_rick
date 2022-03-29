from app.model.comment import Comment
from app.adapters.item_table import AdapterItem

class AdapterComment(AdapterItem):
    def __init__(self, database) -> None:
        super().__init__(database = database, item="comments", model=Comment)
    

    #CREATE
    def create_comment(self, **kwargs):
        columns = []
        valuePlaceholders = []
        values = []
        for column, value in kwargs.items():
            columns.append(column)
            valuePlaceholders.append('%s')
            values.append(value)

        #A changer la requete
        query = "INSERT INTO comments ({}) VALUES ({})".format(', '.join(columns), ', '.join(valuePlaceholders))
        print(query)
        self.database.cur.execute(query, values)
        self.database.conn.commit()
        return "success"


    #READ
    def get_by_id_character(self, id_character:int):
        query = "SELECT * FROM %s WHERE id_character=%s"
        self.database.cur.execute(query, (self.item, id_character))
        return self.model.generate(self.database.cur.fetchall())


    def get_by_id_episode(self, id_episode:int):
        query = "SELECT * FROM %s WHERE id_episode=%s"
        self.database.cur.execute(query, (self.item, id_episode))
        return self.model.generate(self.database.cur.fetchall())


    def get_by_id_episode(self, id_character:int, id_episode:int):
        query = "SELECT * FROM %s WHERE id_character and id_episode=%s"
        self.database.cur.execute(query, (self.item, id_character, id_episode))
        return self.model.generate(self.database.cur.fetchall())
    


    #UPDATE
    def update_row(self, id:int, **kwargs):
        columns = []
        columnPlaceholders = []
        valuePlaceholders = []
        values = []
        for column, value in kwargs.items():
            columns.append(column)
            columnPlaceholders.append('\"%s\"')
            valuePlaceholders.append('= \"%s\"')
            values.append(value)

        query = "UPDATE comments SET %s WHERE id = %s".format(', '.join(columnPlaceholders), ', '.join(valuePlaceholders),  id)
        self.database.cur.execute(query, values)
        self.conn.commit()

        return "success"

    
    #DELETE
    def delete_row(self, id:int):
        query = "DELETE FROM comments WHERE id=%s".format(id)
        self.cur.execute(query)
        self.conn.commit()


