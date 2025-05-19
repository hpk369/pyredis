# main.py
from core.kv_store import KeyValueStore

def run_cli():
    store = KeyValueStore()
    print("Welcome to PyRedis - In-Memory Key-Value Store (Phase 1)")
    while True:
        try:
            command = input("> ").strip()
            if not command:
                continue
            parts = command.split()
            cmd = parts[0].upper()

            if cmd == "SET" and len(parts) == 3:
                store.set(parts[1], parts[2])
                print("OK")
            elif cmd == "GET" and len(parts) == 2:
                result = store.get(parts[1])
                print(result if result is not None else "(nil)")
            elif cmd == "DEL" and len(parts) == 2:
                deleted = store.delete(parts[1])
                print("(1)" if deleted else "(0)")
            elif cmd == "FLUSHALL":
                store.flush_all()
                print("OK")
            elif cmd in ["EXIT", "QUIT"]:
                print("Exiting PyRedis...")
                break
            else:
                print("Invalid command or arguments.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_cli()