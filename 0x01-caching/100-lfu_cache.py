#!/usr/bin/env python3
""" LFUCache module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize the LFUCache
        """
        super().__init__()
        self.frequency = {}
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            keys_to_remove = [k for k, v in self.frequency.items() if v == min_freq]
            if len(keys_to_remove) > 1:
                lru_key = min(self.queue, key=lambda x: self.frequency.get(x, 0))
                keys_to_remove.remove(lru_key)
                print("DISCARD:", lru_key)
            for k in keys_to_remove:
                del self.cache_data[k]
                del self.frequency[k]
                self.queue.remove(k)

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] = self.frequency.get(key, 0) + 1

        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = LFUCache()
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
    my_cache.print_cache()
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()

