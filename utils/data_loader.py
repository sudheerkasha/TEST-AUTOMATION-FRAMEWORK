import json
from pathlib import Path

_DATA_FILE = Path(__file__).resolve().parent.parent / "config" / "test_data.json"


def load_all():
    with open(_DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


def get(key):
    return load_all()[key]


def invalid_login_matrix():
    rows = get("invalid_login_matrix")
    return [(r["id"], r["email"], r["password"], r["desc"]) for r in rows]
