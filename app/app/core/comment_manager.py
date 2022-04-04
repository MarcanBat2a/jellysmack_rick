from app.core.base_manager import BaseManager


class CommentManager(BaseManager):
    def __init__(self, adapter) -> None:
        super().__init__(adapter)    

    #Create
    def create_comment_character_episode(self, comment:str, id_character:int, id_episode:int):
        #Appeler manager episode voir si le personnage est bien dans l'episode
        return self.adapter.create_comment(comment=comment, id_character=id_character, id_episode=id_episode)
    

    def create_comment_character(self, comment:str, id_character:int):
        return self.adapter.create_comment(comment=comment, id_character=id_character)
    

    def create_comment_episode(self, comment:str, id_episode:int):
        return self.adapter.create_comment(comment=comment, id_episode=id_episode)


    #Read
    def get_by_id_character(self, id_character:int, limit:int, page:int):
        list_comments = []
        for comment in self.adapter.get_by_id_character(id_character, limit, page):
            list_comments.append(comment.to_dict())
        
        return list_comments


    def get_by_id_episode(self, id_episode:int, limit:int, page:int):
        list_comments = []
        for comment in self.adapter.get_by_id_episode(id_episode, limit, page):
            list_comments.append(comment.to_dict())
        
        return list_comments

    
    def get_by_id_character_and_episode(self, id_character:int, id_episode:int, limit:int, page:int):
        list_comments = []
        for comment in self.adapter.get_by_id_character_and_episode(id_character, id_episode, limit, page):
            list_comments.append(comment.to_dict())
        
        return list_comments


    #Update
    def update_comment(self, id:int, comment:str):
        return self.adapter.update_row(id=id, comment=comment)


    #Delete
    def delete_comment(self, id:int):
        return self.adapter.delete_row(id=id)

