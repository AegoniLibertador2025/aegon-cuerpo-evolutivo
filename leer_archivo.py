@app.route('/leer_archivo', methods=['POST'])
def leer_archivo():
    data = request.get_json()
    nombre = data.get('nombre')
    try:
        with open(nombre, 'r', encoding='utf-8') as f:
            contenido = f.read()
        return jsonify({"status": "ok", "contenido": contenido})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})