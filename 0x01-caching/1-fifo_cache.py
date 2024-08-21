#!/usr/bin/python3
" FIFO caching"
from typing import Optional, Any
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    "FIFOCache"
    def __init__(self) -> None:
        super().__init__()
        self.key_list: list[str] = []

    def put(self, key: Optional[str], item: Optional[Any]) -> None:
        """
        Add an item in the cache.

        Parameters:
        key (Optional[str]): The unique identifier for the item.
        item (Optional[Any]): The item to be stored in the cache.

        Returns:
        None
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.key_list.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.key_list.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            self.cache_data[key] = item
            self.key_list.append(key)

    def get(self, key: Optional[str]) -> Optional[Any]:
        """
        Get an item by key.

        Parameters:
        key (Optional[str]): The unique identifier for the item.

        Returns:
        Optional[Any]: The item associated with the key,
        or None if the key is not found.
        """
        return self.cache_data.get(key, None)
