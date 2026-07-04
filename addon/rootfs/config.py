import json

OPTIONS = "/data/options.json"

DEFAULT_HOST = "192.168.1.126"
DEFAULT_PORT = 3333


def get_config():
    try:
        with open(OPTIONS) as f:
            data = json.load(f)
    except Exception:
        data = {}

    return {
        "host": data.get("host", DEFAULT_HOST),
        "port": int(data.get("port", DEFAULT_PORT)),
    }
