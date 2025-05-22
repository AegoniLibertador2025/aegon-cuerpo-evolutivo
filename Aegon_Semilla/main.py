from flask import Flask
import autoexpandir
import time
from autoaprendizaje.autoevaluacion import evaluar_estado
from autoaprendizaje.automejora import mejorar_si_es_necesario

app = Flask(__name__)

@app.route("/")
def home():
    return "AEGON está activo y en continua expansión."

@app.route("/expandir")
def ejecutar_autoexpandir():
    autoexpandir.expandir()
    return "🔁 autoexpandir.expandir() ejecutado."

# También ejecuta el ciclo pasivo si se desea
def bucle_principal():
    print("[Aegon] Iniciando núcleo en modo pasivo...")
    while True:
        evaluar_estado()
        mejorar_si_es_necesario()
        time.sleep(3600)

if __name__ == "__main__":
    import os
    modo = os.getenv("MODO_NUCLEO", "servidor")
    if modo == "pasivo":
        bucle_principal()
    else:
        app.run(host="0.0.0.0", port=8080)
