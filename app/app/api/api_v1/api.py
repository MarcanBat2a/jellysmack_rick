from fastapi import APIRouter

from app.api.api_v1.endpoints import character, comment, episode

api_router = APIRouter()
api_router.include_router(episode.router, prefix="/episodes", tags=["Episodes"])
api_router.include_router(character.router, prefix="/characters", tags=["Characters"])
api_router.include_router(comment.router, prefix="/comments", tags=["Comments"])
