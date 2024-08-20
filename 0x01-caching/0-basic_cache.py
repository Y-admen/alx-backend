#!/usr/bin/python3
" Basic dictionary"
from basecaching.base_caching import BaseCaching


class BasicCache(BaseCaching):
    "BasicCache"
    def __init__(self):
        super().__init__()
        self.cache_data = {}

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
