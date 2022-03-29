from app.model.episode import Episode
from app.adapters.item_table import AdapterItem

class AdapterEpisode(AdapterItem):
    def __init__(self, database) -> None:
        super().__init__(database = database, item="episodes", model=Episode)
    
