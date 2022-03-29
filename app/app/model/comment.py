class Comment():
    def __init__(self, id:int, id_character:int, id_comment:int, comment:str) -> None:
        self.id = id
        self.id_character = id_character
        self.id_comment = id_comment
        self.comment = comment
    

    def __init__(self, id:int, id_character:int, comment:str) -> None:
        self.id = id
        self.id_character = id_character
        self.comment = comment
    

    def __init__(self, id:int, id_comment:int, comment:str) -> None:
        self.id = id
        self.id_comment = id_comment
        self.comment = comment
    
    
    @staticmethod
    def generate(comment:dict):
        return Comment(
            id = comment.get('id'),
            id_character = comment.get('id_character'),
            id_episode = comment.get('id_episode'),
            comment = comment.get('comment')
        )

    
    def to_dict(self):
        return {"id": self.id,
                "id_character": self.id_character,
                "id_comment": self.id_comment,
                "comment": self.comment}