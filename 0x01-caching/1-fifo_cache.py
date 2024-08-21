#!/usr/bin/python3
" FIFO caching"
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    "FIFOCache"
    def __init__(self):
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        "add item"
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
