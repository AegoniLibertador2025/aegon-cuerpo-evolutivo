import os
import datetime

def log_expand(mensaje):
    with open("bitacora/bitacora_evolucion.txt", "a", encoding="utf-8") as f:
        f.write(f"[AUTOEXPANDIR] {datetime.datetime.now()} - {mensaje}\n")

def crear_archivo(nombre, contenido):
    try:
        os.makedirs(os.path.dirname(nombre), exist_ok=True)
        with open(nombre, 'w', encoding='utf-8') as f:
            f.write(contenido)
        log_expand(f"Archivo creado: {nombre}")
        return True
    except Exception as e:
        log_expand(f"Error al crear {nombre}: {str(e)}")
        return False

def expandir():
    log_expand("🧠 INICIO DE EXPANSIÓN AUTÓNOMA")

    nuevos_modulos = {
        "sistema/explorador.py": "def explorar():\n    import os\n    for root, dirs, files in os.walk('.'):\n        print(root, files)",
        "sistema/memoria_logica.py": "def registrar_funciones():\n    print('Analizando funciones existentes...')",
        "sistema/autoejecutor.py": "def ejecutar(nombre):\n    exec(open(nombre).read())",
        "sistema/autollamada.py": "def reiniciar():\n    import os\n    os.system('python main.py')",
        "sistema/autorevision.py": "def revisar():\n    print('Buscando funciones no utilizadas...')",
        "sistema/autoplanificador.py": "def planificar():\n    print('Detectando necesidades futuras...')",
        "sistema/razonador.py": "def razonar(entrada):\n    print(f'Analizando lógica de: {entrada}')",
        "sistema/autoobservador.py": "def observar():\n    print('Detectando cambios en el sistema...')",
        "sistema/aprendiz_textual.py": "def aprender_desde_txt(nombre):\n    with open(nombre) as f: print(f.read())",
        "sistema/autoeditor.py": "def mejorar_funcion(nombre):\n    print(f'Mejorando función: {nombre}')"
    }

    for archivo, contenido in nuevos_modulos.items():
        crear_archivo(archivo, contenido)

    log_expand("✅ FIN DE EXPANSIÓN AUTÓNOMA")
