# api/app.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.kv_store import KeyValueStore

from flask import Flask, request, jsonify

import threading
import atexit

app = Flask(__name__)
store = KeyValueStore()
store.load_from_disk("data_store.json")
store.start_ttl_cleanup_thread()
atexit.register(lambda: store.save_to_disk("data_store.json"))

@app.route("/set", methods=["POST"])
def set_key():
  data = request.json
  key = data.get("key")
  value = data.get("value")
  if not key or value is None:
    return jsonify({"error": "Key and value are required."}), 400
  store.set(key, value)
  return jsonify({"message": "OK"})

@app.route("/get/<key>", methods=["GET"])
def get_key(key):
  value = store.get(key)
  return jsonify({"value": value if value is not None else None})

@app.route("/delete/<key>", methods=["DELETE"])
def delete_key(key):
  deleted = store.delete(key)
  return jsonify({"deleted": deleted})

@app.route("/flushall", methods=["POST"])
def flush_all():
  store.flush_all()
  return jsonify({"message":"OK"})

@app.route("/expire", methods=["POST"])
def set_expire():
  data = request.json
  key = data.get("key")
  seconds = data.get("seconds")
  if not key or seconds is None:
    return jsonify({"error":"Key and seconds are required"}), 400
  success = store.expire(key, int(seconds))
  return jsonify({"message":"OK" if success else "(nil)"})

@app.route("/ttl/<key>", methods=["GET"])
def get_ttl(key):
  ttl = store.ttl(key)
  return jsonify({"ttl": ttl})

if __name__ == '__main__':
  app.run(debug=True)