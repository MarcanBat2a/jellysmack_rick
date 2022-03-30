class Comment():
    def __init__(self, id:int, id_character:int, id_episode:int, comment:str) -> None:
        self.id = id
        self.id_character = id_character
        self.id_episode = id_episode
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
                "id_episode": self.id_episode,
                "comment": self.comment}