import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "products.json"


def load_products():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


products = load_products()