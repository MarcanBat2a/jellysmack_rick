from math import ceil

from app.adapters.base_table import AdapterBase
from app.adapters.episode_table import AdapterEpisode
from app.model.comment import Comment


class AdapterComment(AdapterBase):
    COLUMNS = ["id",
            "comment",
            "id_character",
            "id_episode"]

    def __init__(self) -> None:
        super().__init__(item="comments", model=Comment)


    #CREATE
    def create_comment(self, **kwargs):
        if "id_episode" in kwargs.keys() and "id_character" in kwargs.keys():
            episode = AdapterEpisode()
            list_id_characters_on_episode = episode.get_by_id_all_characters(kwargs.get("id_episode"))
            if kwargs.get("id_character") not in list_id_characters_on_episode:
                return "ERROR"
        columns = []
        value_placeholders = []
        values = []
        for column, value in kwargs.items():
            columns.append(column)
            value_placeholders.append('%s')
            values.append(value)
        query = "INSERT INTO comments (air_date, {}) VALUES (NOW(), {})".format(', '.join(columns), ', '.join(value_placeholders))
        self.database.cur.execute(query, values)
        self.database.conn.commit()
        return "success"


    #READ
    def get_by_id_character(self, id_character:int, limit:int, num_page:int)->list:
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


    def get_by_id_episode(self, id_episode:int, limit:int, num_page:int)->list:
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


    def get_by_id_character_and_episode(self, id_character:int, id_episode:int, limit:int, num_page:int)->list:
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


    def get_all_with_filter_pagination(self, limit: int, num_page:int, list_all_filters:str)->list:
        query = "SELECT * FROM comments"
        values_filer = []
        placeholder_params_pagine = []
        if len(list_all_filters) > 0:
            query_filter, values_filer = self.parse_filter(list_all_filters)
            query += query_filter
        if limit != 0 and num_page != 0:
            self.database.cur.execute("SELECT COUNT(*) FROM comments", values_filer)
            total_rows = self.database.cur.fetchall()[0].get("count")
            total_page = ceil(total_rows/limit)
            query_pagine, placeholder_params_pagine = self.pagination(limit, num_page)
            query += query_pagine
        placeholder_params = values_filer + placeholder_params_pagine
        self.database.cur.execute(query, placeholder_params)
        comment_records = self.database.cur.fetchall()
        list_comments = []
        for comment in comment_records:
            list_comments.append(self.model.generate(comment))

        return list_comments, total_page


    #UPDATE
    def update_row(self, id_comment:int, comment:str):
        query = "UPDATE comments SET comment = %s WHERE id = %s"
        self.database.cur.execute(query, (comment, id_comment))
        self.database.conn.commit()

        return "success"


    #DELETE
    def delete_row(self, id_comment:int):
        query = "DELETE FROM comments WHERE id=%s"
        self.database.cur.execute(query, (id_comment,))
        self.database.conn.commit()
        return "success"
