import os

def crear_archivo(nombre, contenido):
    with open(nombre, 'w', encoding='utf-8') as f:
        f.write(contenido)
