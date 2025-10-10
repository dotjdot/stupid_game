

class collections:
    def __init__(self):
        collection_dict = {}
        return
    
    def add_to_collection(self, item, quantity):
        if item in self.collection_dict:
            self.collection_dict[item] += quantity
        else:
            self.collection_dict[item] = quantity

    def remove_from_collection(self, item, quantity):
        if item in self.collection_dict:
            if self.collection_dict[item] >= quantity:
                self.collection_dict[item] -= quantity
                return True
            else:
                return False
        else:
            return False
    
