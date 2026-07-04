from pathlib import Path
import json

CONFIG = Path("/data/programmers.json")

if not CONFIG.exists():
    CONFIG.write_text("[]")


def load():
    return json.loads(CONFIG.read_text())


def save(data):
    CONFIG.write_text(json.dumps(data, indent=2))


def all():
    return load()


def add(host, port, name):
    data = load()
    data.append({
        "name": name,
        "host": host,
        "port": port,
    })
    save(data)
