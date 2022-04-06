from fastapi import APIRouter
from app.core.episode_manager import EpisodeManager
from app.adapters.episode_table import AdapterEpisode

adapter = AdapterEpisode()
episode_manager = EpisodeManager(adapter)

router = APIRouter()

@router.get("/")
def read_episodes():
    return episode_manager.get_all()