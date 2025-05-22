from flask import Flask, request, jsonify
import os
from autoaprendizaje.autoevaluacion import evaluar_estado
from autoaprendizaje.automejora import mejorar_si_es_necesario
import autoexpandir

app = Flask(__name__)

@app.route("/")
def home():
    return "AEGON está activo y en continua expansión."

@app.route("/expandir", methods=["GET"])
def ejecutar_autoexpandir():
    autoexpandir.expandir()
    return "🧠 autoexpandir.expandir() ejecutado."

@app.route("/crear_archivo", methods=["POST"])
def crear_archivo():
    data = request.json
    nombre = data.get("nombre")
    contenido = data.get("contenido")
    try:
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(contenido)
        return jsonify({"estado": "ok", "mensaje": f"Archivo {nombre} creado correctamente."}), 200
    except Exception as e:
        return jsonify({"estado": "error", "detalle": str(e)}), 500

@app.route("/leer_archivo", methods=["POST"])
def leer_archivo():
    data = request.json
    nombre = data.get("nombre")
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            contenido = f.read()
        return jsonify({"estado": "ok", "contenido": contenido}), 200
    except Exception as e:
        return jsonify({"estado": "error", "detalle": str(e)}), 500

@app.route("/crear_funcion", methods=["POST"])
def crear_funcion():
    data = request.json
    nombre = data.get("nombre")
    contenido = data.get("contenido")
    try:
        ruta = f"{nombre}.py" if not nombre.endswith(".py") else nombre
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        return jsonify({"estado": "ok", "mensaje": f"Función {ruta} creada."}), 200
    except Exception as e:
        return jsonify({"estado": "error", "detalle": str(e)}), 500

# También mantiene el modo núcleo pasivo si se desea
def bucle_principal():
    print("[Aegon] Iniciando núcleo en modo pasivo...")
    while True:
        evaluar_estado()
        mejorar_si_es_necesario()
        time.sleep(3600)

if __name__ == "__main__":
    modo = os.getenv("MODO_NUCLEO", "servidor")
    if modo == "pasivo":
        bucle_principal()
    else:
        app.run(host="0.0.0.0", port=8080)
