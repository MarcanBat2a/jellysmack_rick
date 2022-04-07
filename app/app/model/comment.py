class Comment():
    def __init__(self, id_comment:int, id_character:int, id_episode:int, comment:str, date:str) -> None:
        self.id_comment = id_comment
        self.id_character = id_character
        self.id_episode = id_episode
        self.comment = comment
        self.date = date


    @staticmethod
    def generate(comment:dict):
        return Comment(
            id_comment = comment.get('id'),
            id_character = comment.get('id_character'),
            id_episode = comment.get('id_episode'),
            comment = comment.get('comment'),
            date = comment.get('air_date')
        )


    def to_dict(self):
        return {"id_comment": self.id_comment,
                "id_character": self.id_character,
                "id_episode": self.id_episode,
                "comment": self.comment,
                "date": self.date}
