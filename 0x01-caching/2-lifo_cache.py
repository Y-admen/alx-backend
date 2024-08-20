#!/usr/bin/python3
" LIFO Cache"
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    "LIFOCache"
    def __init__(self):
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        "add item"
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop()
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))

    def get(self, key):
        "get vlaue"
        if not key or key not in self.cache_data:
            return
        return self.cache_data[key]
