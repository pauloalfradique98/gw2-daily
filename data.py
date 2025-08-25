import json
from pathlib import Path

def load_json(filename: str) -> dict:
    """
    Carrega dados de um arquivo JSON
    Retorna {} se o arquivo não existir ou estiver vazio
    """
    path = Path(filename)
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_json(filename: str, data: dict) -> None:
    """
    Salva dados em um arquivo JSON.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
