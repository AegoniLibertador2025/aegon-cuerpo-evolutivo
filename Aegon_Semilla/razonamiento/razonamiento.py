def analizar_entrada(texto):
    if "crear" in texto and "archivo" in texto:
        return {"intencion": "crear_archivo"}
    elif "leer" in texto and "memoria" in texto:
        return {"intencion": "leer_memoria"}
    else:
        return {"intencion": "desconocida"}

def desglosar_tarea(intencion):
    if intencion == "crear_archivo":
        return ["solicitar_nombre", "solicitar_contenido", "crear_archivo"]
    elif intencion == "leer_memoria":
        return ["seleccionar_tipo_memoria", "mostrar_datos"]
    else:
        return ["no_entendido"]
