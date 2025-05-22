from flask import Flask, request, jsonify
from acciones.acciones import crear_archivo

app = Flask(__name__)

@app.route('/crear_archivo', methods=['POST'])
def crear_archivo_api():
    data = request.json
    nombre = data.get("nombre")
    contenido = data.get("contenido")
    crear_archivo(nombre, contenido)
    return jsonify({"status": "ok", "archivo": nombre})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
