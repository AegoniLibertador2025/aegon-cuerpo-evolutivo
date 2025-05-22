import json

def cargar_memoria(tipo):
    with open(f"memoria/{tipo}_plazo.json", "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_memoria(tipo, datos):
    with open(f"memoria/{tipo}_plazo.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)
