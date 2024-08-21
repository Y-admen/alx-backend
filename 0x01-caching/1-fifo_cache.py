#!/usr/bin/python3
" FIFO caching"
from typing import Optional, Any
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    "FIFOCache"
    def __init__(self)-> None:
        super().__init__()
        self.key_list: list[str] = []

# Optional[X] is a shorthand for Union[X, None]/in str can not be None
    def put(self, key: Optional[str], item: Optional[Any])-> None:
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.key_list.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.key_list.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key: Optional[str])-> Optional[Any]:
        """ Get an item by key """
        return self.cache_data.get(key, None)
