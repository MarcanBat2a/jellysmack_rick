from abc import ABC


class BaseManager(ABC):
    def __init__(self, adapter) -> None:
        self.adapter = adapter
    

    def get_all(self):
        list_object = []
        for adapter in self.adapter.get_all():
            list_object.append(adapter.to_dict())
        
        return list_object
    

    def get_all_with_filter_pagination(self, limit, num_page, filter):
        list_object = []
        for adapter in self.adapter.get_all_with_filter_pagination(limit, num_page, filter):
            list_object.append(adapter.to_dict())
        
        return list_object

    
    def get_by_id(self, id):
        return self.adapter.get_by_id(id).to_dict()