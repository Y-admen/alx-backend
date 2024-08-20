#!/usr/bin/python3
" Basic dictionary"
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    "BasicCache"
    def put(self, key, item):
        "add item"
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        "get vlaue"
        if not key or key not in self.cache_data:
            return
        return self.cache_data[key]
