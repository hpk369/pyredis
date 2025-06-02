# gui/web_gui.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from core.kv_store import KeyValueStore
import atexit

app = Flask(__name__,)

store = KeyValueStore()
store.load_from_disk("data_store.json")
store.start_ttl_cleanup_thread()
atexit.register(lambda: store.save_to_disk("data_store.json"))

@app.route("/", methods=["GET", "POST"])
def index():
  result = ""
  value = ""
  key_input = ""
  val_input = ""
  if request.method == "POST":
    action = request.form.get("action")
    key_input = request.form.get("key")
    val_input = request.form.get("value")

    if action == "set" and key_input and val_input is not None:
      store.set(key_input, val_input)
      result = "OK"
    elif action == "get" and key_input:
      value = store.get(key_input) or ""
    elif action == "del" and key_input:
      deleted = store.delete(key_input)
      result = f"Deleted: {deleted}"
    elif action == "flush":
      store.flush_all()
      result = "OK"
    
  return render_template("index.html", result=result, value=value, key_input=key_input, val_input=val_input)
  
if __name__ == '__main__':
    port = 9567
    print(f"Running PyRedis Web GUI on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)