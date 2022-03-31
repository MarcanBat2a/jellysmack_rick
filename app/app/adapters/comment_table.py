from app.model.comment import Comment
from app.adapters.item_table import AdapterItem
from app.adapters.episode_table import AdapterEpisode

class AdapterComment(AdapterItem):
    def __init__(self, database) -> None:
        super().__init__(database = database, item="comments", model=Comment)
    

    #CREATE
    def create_comment(self, **kwargs):
        if "id_episode" in kwargs.keys() and "id_character" in kwargs.keys():
            episode = AdapterEpisode(self.database)
            list_id_characters_on_episode = episode.get_by_id_all_characters(kwargs.get("id_episode"))
            if kwargs.get("id_character") not in list_id_characters_on_episode:
                return "ERROR"
      
        columns = []
        valuePlaceholders = []
        values = []
        for column, value in kwargs.items():
            columns.append(column)
            valuePlaceholders.append('%s')
            values.append(value)

        query = "INSERT INTO comments ({}) VALUES ({})".format(', '.join(columns), ', '.join(valuePlaceholders))
        self.database.cur.execute(query, values)
        self.database.conn.commit()
        return "success"


    #READ
    def get_all(self, limit:int, num_page:int):
        if limit != 0 and num_page != 0:
            offset = limit*(num_page-1)
            query = "SELECT * FROM comments LIMIT %s OFFSET %s"
            self.database.cur.execute(query, (limit, offset))
        else:
            query = "SELECT * FROM comments"
            self.database.cur.execute(query)
        character_records = self.database.cur.fetchall()
        list_comments = []
        for character in character_records:
            list_comments.append(self.model.generate(character))
        return list_comments


    def get_by_id_character(self, id_character:int, limit:int, num_page:int):
        if limit != 0 and num_page != 0:
            offset = limit*(num_page-1)
            query = "SELECT * FROM comments WHERE id_character=%s LIMIT %s OFFSET %s"
            self.database.cur.execute(query, (id_character, limit, offset))
        else:
            query = "SELECT * FROM comments WHERE id_character=%s"
            self.database.cur.execute(query, (id_character,))
        comment_records = self.database.cur.fetchall()
        list_comments = []

        for comment in comment_records:
            list_comments.append(self.model.generate(comment))
        return list_comments


    def get_by_id_episode(self, id_episode:int, limit:int, num_page:int):
        if limit != 0 and num_page != 0:
            offset = limit*(num_page-1)
            query = "SELECT * FROM comments WHERE id_episode=%s LIMIT %s OFFSET %s"
            self.database.cur.execute(query, (id_episode, limit, offset))
        else:     
            query = "SELECT * FROM comments WHERE id_episode=%s"
            self.database.cur.execute(query, (id_episode,))
        comment_records = self.database.cur.fetchall()
        list_comments = []
        for comment in comment_records:
            list_comments.append(self.model.generate(comment))
        return list_comments


    def get_by_id_character_and_episode(self, id_character:int, id_episode:int, limit:int, num_page:int):
        if limit != 0 and num_page != 0:
            offset = limit*(num_page-1)
            query = "SELECT * FROM comments WHERE id_character=%s and id_episode=%s LIMIT %s OFFSET %s"
            self.database.cur.execute(query, (id_character, id_episode, limit, offset))
        else:
            query = "SELECT * FROM comments WHERE id_character=%s and id_episode=%s"
            self.database.cur.execute(query, (id_character, id_episode))
        comment_records = self.database.cur.fetchall()
        list_comments = []
        for comment in comment_records:
            list_comments.append(self.model.generate(comment))
        return list_comments


    #UPDATE
    def update_row(self, id:int, comment:str):
        query = "UPDATE comments SET comment = %s WHERE id = %s"
        self.database.cur.execute(query, (comment, id))
        self.database.conn.commit()

        return "success"

    
    #DELETE
    def delete_row(self, id:int):
        query = "DELETE FROM comments WHERE id={}".format(id)
        self.database.cur.execute(query)
        self.database.conn.commit()
        return "success"


