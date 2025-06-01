# tests/test_kv_store.py

from core.kv_store import KeyValueStore

import unittest
import time
import os


class TestKeyValueStore(unittest.TestCase):
    def setUp(self):
        self.kv = KeyValueStore()
        self.kv.start_ttl_cleanup_thread()

    def test_set_and_get(self):
        # Test setting and retrieving a key-value pair
        self.kv.set("name", "devam")
        self.assertEqual(self.kv.get("name"), "devam")

    def test_get_nonexistent(self):
        # Test getting a key that doesn't exist
        self.assertIsNone(self.kv.get("age"))

    def test_delete(self):
        # Test deleting a key
        self.kv.set("key", "value")
        self.assertTrue(self.kv.delete("key"))
        self.assertIsNone(self.kv.get("key"))

    def test_flush_all(self):
        # Test clearing the store
        self.kv.set("a", "1")
        self.kv.set("b", "2")
        self.kv.flush_all()
        self.assertIsNone(self.kv.get("a"))
        self.assertIsNone(self.kv.get("b"))

    def test_expire_and_ttl(self):
        # Test expiration and time-to-live
        self.kv.set("temp", "data")
        self.assertTrue(self.kv.expire("temp", 2))
        ttl = self.kv.ttl("temp")
        self.assertTrue(ttl > 0)
        time.sleep(3)
        self.assertIsNone(self.kv.get("temp"))
        self.assertEqual(self.kv.ttl("temp"), -1)

    def test_save_and_load_from_disk(self):
        test_file = "test-data.json"

        # Set and save data
        self.kv.set("framework", "flask")
        self.kv.expire("framework", 10)
        self.kv.save_to_disk(test_file)

        # Load data into a new instance
        new_kv = KeyValueStore()
        new_kv.load_from_disk(test_file)

        # Validate persistence
        self.assertEqual(new_kv.get("framework"), "flask")
        self.assertTrue(new_kv.ttl("framework") > 0)

        # Clean up
        os.remove(test_file)

if __name__ == '__main__':
    unittest.main()