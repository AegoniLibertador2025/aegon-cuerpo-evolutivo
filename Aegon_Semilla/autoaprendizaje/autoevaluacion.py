from memoria.memoria import cargar_memoria

def evaluar_estado():
    memoria = cargar_memoria("largo")
    if len(memoria["aprendizajes"]) < 3:
        print("[Autoevaluación] Pocos aprendizajes registrados. Considerar mejorar estructura.")
    else:
        print("[Autoevaluación] Memoria larga saludable.")
