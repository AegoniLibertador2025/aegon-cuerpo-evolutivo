@app.route('/crear_funcion', methods=['POST'])
def crear_funcion():
    data = request.get_json()
    nombre = data.get('nombre')
    codigo = data.get('codigo')
    if not nombre.endswith('.py'):
        return jsonify({"status": "error", "error": "El archivo debe terminar en .py"})
    try:
        with open(nombre, 'w', encoding='utf-8') as f:
            f.write(codigo)
        return jsonify({"status": "ok", "archivo": nombre})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})