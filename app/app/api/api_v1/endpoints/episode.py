from fastapi import APIRouter
from app.core.episode_manager import EpisodeManager
from app.adapters.episode_table import AdapterEpisode
from app.adapters.postgres.client import Database

# Cest de la merde à voir pour eviter la redondance des imports dans main
database = Database()
adapter = AdapterEpisode(database)
episode_manager = EpisodeManager(adapter)
# Cest de la merde à voir pour eviter la redondance des imports


router = APIRouter()

@router.get("/")
def read_episodes():
    return episode_manager.get_all(), 200