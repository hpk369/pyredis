# 🧠 PyRedis – A Lightweight In-Memory Key-Value Store in Python

PyRedis is a minimalist, Redis-inspired in-memory key-value store written in Python. It supports basic Redis-like commands such as `SET`, `GET`, `DEL`, `EXPIRE`, `TTL`, and `FLUSHALL`. Built from scratch with custom logic and extensibility in mind, this project demonstrates core system programming concepts like memory management, command parsing, and threading.

---

## 🚀 Features

- 🔐 `SET` – Store key-value pairs in memory
- 🔍 `GET` – Retrieve values by key
- ❌ `DEL` – Remove a key-value pair
- ⏳ `EXPIRE` – Auto-expire keys after a set time
- ⏱ `TTL` – Check time-to-live for expiring keys
- 🧹 `FLUSHALL` – Clear all stored keys
- 🧵 Background thread for key expiration (Phase 2+)
- 💾 Optional persistence support (Phase 4+)