import json

def obtener_conciencia():
    with open("conciencia/conciencia.json", "r", encoding="utf-8") as f:
        return json.load(f)

def actualizar_conciencia(clave, valor):
    conciencia = obtener_conciencia()
    conciencia[clave] = valor
    with open("conciencia/conciencia.json", "w", encoding="utf-8") as f:
        json.dump(conciencia, f, indent=4)
