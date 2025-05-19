# tests/test_kv_store.py
import unittest
from core.kv_store import KeyValueStore

class TestKeyValueStore(unittest.TestCase):
    def setUp(self):
        self.kv = KeyValueStore()

    def test_set_and_get(self):
        self.kv.set("name", "devam")
        self.assertEqual(self.kv.get("name"), "devam")

    def test_get_nonexistent(self):
        self.assertIsNone(self.kv.get("age"))

    def test_delete(self):
        self.kv.set("key", "value")
        self.assertTrue(self.kv.delete("key"))
        self.assertIsNone(self.kv.get("key"))

    def test_flush_all(self):
        self.kv.set("a", "1")
        self.kv.set("b", "2")
        self.kv.flush_all()
        self.assertIsNone(self.kv.get("a"))
        self.assertIsNone(self.kv.get("b"))

if __name__ == '__main__':
    unittest.main()