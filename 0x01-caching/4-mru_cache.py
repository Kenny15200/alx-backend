#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize the MRUCache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.queue.pop()
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.queue.remove(key)
        self.queue.append(key)

        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = MRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")

