import os
import datetime

def log_expand(mensaje):
    with open("bitacora/bitacora_evolucion.txt", "a", encoding="utf-8") as f:
        f.write(f"[AUTOEXPANDIR] {datetime.datetime.now()} - {mensaje}\n")

def crear_archivo(nombre, contenido):
    try:
        with open(nombre, 'w', encoding='utf-8') as f:
            f.write(contenido)
        log_expand(f"Archivo creado: {nombre}")
        return True
    except Exception as e:
        log_expand(f"Error al crear {nombre}: {str(e)}")
        return False

def expandir():
    log_expand("Inicio de expansión automática")
    nuevas_funciones = {
        "modulo_ejemplo.py": "def saludar():\n    print('Hola desde el módulo expandido')"
    }
    for archivo, contenido in nuevas_funciones.items():
        crear_archivo(archivo, contenido)
    log_expand("Fin de expansión automática")