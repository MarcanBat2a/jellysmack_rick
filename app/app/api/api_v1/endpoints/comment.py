import io
import pandas as pd
from app.adapters.comment_table import AdapterComment
from app.adapters.postgres.client import Database
from app.core.comment_manager import CommentManager
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

# Cest de la merde à voir pour eviter la redondance des imports dans main
database = Database()
adapter = AdapterComment(database)
comment_manager = CommentManager(adapter)
# Cest de la merde à voir pour eviter la redondance des imports


router = APIRouter()
#CREATE
@router.post("/{comment}/characters/{character_id}/episodes/{episode_id}")
def create_comment_on_character_and_episode(comment:str, character_id:int, episode_id:int):
    return comment_manager.create_comment_character_episode(comment, character_id, episode_id), 200


@router.post("/{comment}/episodes/{episode_id}")
def create_comment_on_character_and_episode(comment:str, episode_id:int):
    return comment_manager.create_comment_episode(comment, episode_id), 200


@router.post("/{comment}/characters/{character_id}")
def create_comment_on_character(comment:str, character_id:int):
    return comment_manager.create_comment_character(comment, character_id), 200


#READ
@router.get("/")
def read_comments(limit:int=0, page:int=0, search:str=""):
    if (limit>0 and page>0) or search != "":
        return comment_manager.get_all_with_filter_pagination(limit, page, search), 200
    else:
        return comment_manager.get_all(), 200


@router.get("/characters/{character_id}")
def read_comments_id_character(character_id:int, limit:int=0, page:int=0):
    return comment_manager.get_by_id_character(character_id, limit, page), 200


@router.get("/episodes/{episode_id}")
def read_comments_id_episode(episode_id:int, limit:int=0, page:int=0):
    return comment_manager.get_by_id_episode(episode_id, limit, page), 200


@router.get("/characters/{character_id}/episodes/{episode_id}")
def read_comments_id_character_and_episode(character_id:int, episode_id:int, limit:int=0, page:int=0):
    return comment_manager.get_by_id_character_and_episode(character_id, episode_id, limit, page), 200


#Update
@router.put("/{id}/{comment}")
def update_comment(id:int, comment:str):
    return comment_manager.update_comment(id, comment), 200


#Delete
@router.delete("/{id}")
def delete_comment(id:int):
    return comment_manager.delete_comment(id), 200


@router.get("/export")
def export_comment(format:str):
    list_dataframe_comment = []

    for comment in comment_manager.get_all():
        list_dataframe_comment.append(pd.DataFrame(comment.values()).T)
    
    dataframe_result = pd.concat(list_dataframe_comment, ignore_index=True)
    dataframe_result.columns = comment.keys()

    if format.lower()=="csv":
        stream = io.StringIO()
        dataframe_result.to_csv(stream, index = False)
        response = StreamingResponse(iter([stream.getvalue()]),
                                media_type="text/csv"
        )
        response.headers["Content-Disposition"] = "attachment; filename=export_comment.csv"
    else:
        stream = io.BytesIO()
        writer = pd.ExcelWriter(stream, engine='xlsxwriter')
        dataframe_result.to_excel(writer, index = False)
        writer.save()
        xlsx_data = stream.getvalue()
        response = StreamingResponse(io.BytesIO(xlsx_data), media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response.headers["Content-Disposition"] = "attachment; filename=filename=export.xls"
    return response


