#!/usr/bin/python3
" FIFO caching"
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    "FIFOCache"
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.key_list = []

    def put(self, key, item):
        "add item"
        if not key or not item:
            return
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.key_list.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key):
        "get vlaue"
        if not key or key not in self.cache_data:
            return
        return self.cache_data[key]
