import json
from typing import Any

def save_json(json_data: dict[str, Any], path: str = "data/data.json") -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4)
        
def load_json(path: str = "data/data.json") -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)