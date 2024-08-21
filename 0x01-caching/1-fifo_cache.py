#!/usr/bin/python3
" FIFO caching"
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()  # Call the parent class's constructor

    def put(self, key, item):
        if key is None or item is None:
            return

        # Add the item to the cache
        self.cache_data[key] = item

        # Check if we need to discard the first item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the first inserted key
            first_key = next(iter(self.cache_data))
            # FIFO: first item in the dictionary
            # Remove the first inserted item
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
