#!/usr/bin/python3
" LRU Cache"
from typing import Any
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    "LRUCache"
    def __init__(self) -> None:
        """ Initialize of FIFO and call the base"""
        super().__init__()
        self.lru_keys = []

    def put(self, key, item) -> None:
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
        if key in self.lru_keys:
            self.cache_data[key] = item

            self.lru_keys.remove(key)
            self.lru_keys.append(key)
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            self.cache_data.pop(self.lru_keys[0])
            print(f'DISCARD: {self.lru_keys[0]}')
            self.lru_keys.pop(0)

        self.lru_keys.append(key)
        self.cache_data[key] = item

    def get(self, key) -> Any:
        """
        Get an item by key.

        Parameters:
        key (str): The unique identifier for the item.

        Returns:
        Any: The item associated with the key, or None if the key is not found.
        """
        value = self.cache_data.get(key)
        if value:
            self.lru_keys.remove(key)
            self.lru_keys.append(key)

        return self.cache_data.get(key, None)
