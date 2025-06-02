# README.md

# PyRedis: A Lightweight Redis-like Key-Value Store

PyRedis is a lightweight, persistent key-value store written in Python, designed to simulate Redis-like functionality for learning, local development, or prototyping purposes. It includes a command-line interface, a web GUI powered by Flask, TTL support, disk persistence, and Dockerization for smooth deployment.

---

## Features
- Fast in-memory key-value operations
- TTL (time-to-live) support for expiring keys
- Data persistence using JSON file storage
- Unit tests for reliability and correctness
- Web-based GUI built with Flask
- Docker support for isolated deployment

---

## Technologies Used
- Python 3.10
- Flask - Web GUI
- Docker - Containerization
- HTML/CSS - Simple UI frontend
- argparse - CLI commands
- requests - HTTP handling (optional future enhancements)

---

## How to Run

### Local Setup
```bash
# Clone the repo
cd pyredis
pip install -r requirements.txt
python gui/web_gui.py
```
Then visit: [http://localhost:9567](http://localhost:9567)

### Docker Setup
```bash
# Build the image
docker build -t pyredis-webgui .

# Run the container (on port 5000)
docker run --rm -p 5000:5000 pyredis-webgui
```
Visit: [http://localhost:5000](http://localhost:9567)

---

## Run Tests
```bash
python -m unittest tests/test_kv_store.py
```

---

## Project Structure
```
├── core/
│   └── kv_store.py         # KeyValueStore logic
├── gui/
│   ├── web_gui.py          # Flask web server
│   └── templates/
│       └── index.html      # Frontend HTML interface
├── tests/
│   └── test_kv_store.py    # Unit tests
├── Dockerfile              # Container configuration
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## TODO / Future Enhancements
- Add user authentication to the web GUI
- Add support for namespaces or multiple logical databases
- Add GUI styling with Bootstrap or Tailwind CSS
- Deploy on Render/Fly.io/Heroku

---

Feel free to fork, star, and contribute!
