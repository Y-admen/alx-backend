#!/usr/bin/python3
" LRU Cache"
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    "LRUCache"
    def __init__(self):
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        "add item"
        if not key or not item:
            return
        if key in self.cache_data:
            del self.cache_data[key]
            self.key_list.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.key_list.pop(0)
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")
        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key):
        "get vlaue"
        if not key or key not in self.cache_data:
            return
        value = self.cache_data[key]
        del self.cache_data[key]
        self.key_list.remove(key)
        self.cache_data[key] = value
        self.key_list.append(key)
        return value
