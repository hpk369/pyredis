# main.py

from core.kv_store import KeyValueStore

import argparse
import threading
import time
import atexit

def main():
  # Initialize the CLI parser and accept one or more arguments
  parser = argparse.ArgumentParser(description="PyRedis - In-Memory Key-Value Store")
  parser.add_argument("command", nargs='+', help="Command to run (SET, GET, DEL, EXPIRE, TIL, FLUSHALL)")
  args = parser.parse_args()

  # Create an instance of the store and load saved data if available
  store = KeyValueStore()
  store.load_from_disk("data-store.json")   # Restore previous session data
  store.start_ttl_cleanup_thread()  # Start background thread to monitor key expirations

  # Ensure that data is saved to disk when the program exits
  
  # Read the command and parse its arguments
  cmd_parts = args.command
  cmd = cmd_parts[0].upper()    # Convert to uppercase for uniform handling

  try:
    # Handle each supported command
    if cmd == "SET" and len(cmd_parts) == 3:
      store.set(cmd_parts[1], cmd_parts[2])
      print("OK")
    elif cmd == "GET" and len(cmd_parts) == 2:
      result = store.get(cmd_parts[1])
      print(result if result is not None else "(nil)")
    elif cmd == "DEL" and len(cmd_parts) == 2:
      deleted = store.delete(cmd_parts[1])
      print("(1)" if deleted else "(0)")
    elif cmd == "FLUSHALL":
      store.flush_all()
      print("OK")
    elif cmd == "EXPIRE" and len(cmd_parts) == 3:
      success = store.expire(cmd_parts[1], int(cmd_parts[2]))
      print("OK" if success else "(nil)")
    elif cmd == "TTL" and len(cmd_parts) == 2:
      ttl = store.ttl(cmd_parts[1])
      print(ttl if ttl >= 0 else "(nil)")
    else:
      print("Invalud command or arguments.")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()