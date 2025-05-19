# core/kv_store.py
class KeyValueStore:
    def __init__(self):
        self.store = {}

    def set(self, key, value):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key)

    def delete(self, key):
        return self.store.pop(key, None) is not None

    def flush_all(self):
        self.store.clear()
