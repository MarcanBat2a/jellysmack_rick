from app.core.base_manager import BaseManager

class EpisodeManager(BaseManager):
    def __init__(self, adapter) -> None:
        super().__init__(adapter)
    
