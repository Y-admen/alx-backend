#!/usr/bin/python3
" MRU Cache"
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    "MRUCache"
    def __init__(self):
        """ Initialize of MRU and call the base"""
        super().__init__()
        self.cache_data = {}
        self.key_list = []

    def put(self, key, item):
        """
        Add an item to the cache.

        Parameters:
        key (str): The unique identifier for the item.
        item (Any): The item to be stored in the cache.

        Returns:
        None
        """
        if not key or not item:
            return
        if key in self.cache_data:
            del self.cache_data[key]
            self.key_list.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.key_list.pop()
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")
        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key):
        """
        Get an item by key.

        Parameters:
        key (str): The unique identifier for the item.

        Returns:
        Any: The item associated with the key, or None if the key is not found.
        """
        if not key or key not in self.cache_data:
            return
        value = self.cache_data[key]
        del self.cache_data[key]
        self.key_list.remove(key)
        self.cache_data[key] = value
        self.key_list.append(key)
        return value
