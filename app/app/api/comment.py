from fastapi import APIRouter
from app.core.comment_manager import CommentManager
from app.adapters.comment_table import AdapterComment
from app.adapters.postgres.client import Database

# Cest de la merde à voir pour eviter la redondance des imports dans main
database = Database()
adapter = AdapterComment(database)
comment_manager = CommentManager(adapter)
# Cest de la merde à voir pour eviter la redondance des imports


router = APIRouter()
#CREATE
@router.post("/comments/{comment}/characters/{character_id}/episodes/{episode_id}")
def create_comment_on_character_and_episode(comment:str, character_id:int, episode_id:int):
    return comment_manager.create_comment_character_episode(comment, character_id, episode_id)


@router.post("/comments/{comment}/episodes/{episode_id}")
def create_comment_on_character_and_episode(comment:str, episode_id:int):
    return comment_manager.create_comment_episode(comment, episode_id)


@router.post("/comments/{comment}/characters/{character_id}")
def create_comment_on_character(comment:str, character_id:int):
    return comment_manager.create_comment_character(comment, character_id)


#READ
@router.get("/comments")
def read_comments(limit:int=0, page:int=0):
    return comment_manager.get_all(limit, page), 200


@router.get("/comments/characters/{character_id}")
def read_comments_id_character(character_id:int, limit:int=0, page:int=0):
    return comment_manager.get_by_id_character(character_id, limit, page), 200


@router.get("/comments/episodes/{episode_id}")
def read_comments_id_episode(episode_id:int, limit:int=0, page:int=0):
    return comment_manager.get_by_id_episode(episode_id, limit, page), 200


@router.get("/comments/characters/{character_id}/episodes/{episode_id}")
def read_comments_id_character_and_episode(character_id:int, episode_id:int, limit:int=0, page:int=0):
    return comment_manager.get_by_id_character_and_episode(character_id, episode_id, limit, page), 200


#Update
@router.put("/comments/{id}/{comment}")
def update_comment(id:int, comment:str):
    return comment_manager.update_comment(id, comment)


#Delete
@router.delete("/comment/{id}")
def delete_comment(id:int):
    return comment_manager.delete_comment(id)

