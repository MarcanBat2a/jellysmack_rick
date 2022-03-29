class CommentManager:
    def __init__(self, adapter) -> None:
        self.adapter = adapter
    
    #Create
    def create_comment_character_episode(self, comment:str, id_character:int, id_episode:int):
        
        return self.adapter.create_comment(comment=comment, id_character=id_character, id_episode=id_episode)
    

    def create_comment_character(self, comment:str, id_character:int):
        return self.adapter.create_comment(comment=comment, id_character=id_character)
    

    def create_comment_episode(self, comment:str, id_episode:int):
        return self.adapter.create_comment(comment=comment, id_episode=id_episode)


    #Read
    def get_all(self):
        list_comments = []
        for comment in self.adapter.get_all():
            list_comments.append(comment.to_dict())
        
        return list_comments


    def get_by_id_character(self, id_character:int):
        return self.adapter.get_by_id_character(id_character).to_dict()


    def get_by_id_episode(self, id_episode:int):
        return self.adapter.get_by_id_episode(id_episode).to_dict()

    
    def get_by_id_character_and_episode(self, id_character:int, id_episode:int):
        return self.adapter.get_by_id_character_and_episode(id_character, id_episode).to_dict()


    #Update
    def update_comment(self, id:int, comment:str):
        return self.adapter.update_row(id=id, comment=comment)


    #Delete
    def delete_comment(self, id:int):
        return self.adapter.delete_row(id=id)