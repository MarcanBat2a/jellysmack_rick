from abc import ABC


class BaseManager(ABC):
    def __init__(self, adapter) -> None:
        self.adapter = adapter
    

    def get_all(self):
        list_object = []
        for adapter in self.adapter.get_all():
            list_object.append(adapter.to_dict())
        
        return list_object
    

    def get_all_with_filter_pagination(self, limit:int, num_page:int, filter:str):
        list_object = []
        list_result, total_page = self.adapter.get_all_with_filter_pagination(limit, num_page, filter)
        for adapter in list_result:
            list_object.append(adapter.to_dict())
        
        return list_object, {"total page":total_page}

