# core/kv_store.py

import time
import threading

class KeyValueStore:
    def __init__(self):
        self.store = {} # Dictionary to store key-value pairs
        self.expirations = {}   # Dictionary to track expiration times
        self.lock = threading.Lock()    # Lock to ensure thread-safe access

    def set(self, key, value):
        # Store the key-value pairs and remove any expiration
        with self.lock:
            self.store[key] = value
            if key in self.expirations:
                del self.expirations[key]

    def get(self, key):
        # Retrieve value if not expired, else return None
        with self.lock:
            if key in self.expirations and time.time() >= self.expirations[key]:
                self._expire_key(key)
                return None
            return self.store.get(key)

    def delete(self, key):
        # Remove the key from both store and expiration map
        with self.lock:
            existed = key in self.store
            self.store.pop(key, None)
            self.expirations.pop(key, None)
            return existed

    def flush_all(self):
        # Clear all the stored data
        with self.lock:
            self.store.clear()
            self.expirations.clear()

    def expire(self, key, seconds):
        # Set the expiration time for a key
        with self.lock:
            if key in self.store:
                self.expirations[key] = time.time() + seconds
                return True
            return False
        
    def ttl(self, key):
        # Return the time-to-live for a key, or -1 if not expiring
        with self.lock:
            if key in self.expirations:
                ttl = int(self.expirations[key] - time.time())
                return ttl if ttl > 0 else -1
            return -1
        
    def _expire_key(self, key):
        # Internally expire a key
        self.store.pop(key, None)
        self.expirations.pop(key, None)
        
    def start_ttl_cleanup_thread(self):
        # Start background thread to check and expire keys periodically
        def cleanup():
            while True:
                time.sleep(1)
                current_time = time.time()
                with self.lock:
                    expired_keys = [key for key, exp in self.expirations.items() if current_time >= exp]
                    for key in expired_keys:
                        self._expire_key(key)

        thread = threading.Thread(target=cleanup, daemon=True)
        thread.start()
