from app.core.base_manager import BaseManager

class CharacterManager(BaseManager):
    def __init__(self, adapter) -> None:
        super().__init__(adapter)
