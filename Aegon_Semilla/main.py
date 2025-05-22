import time
from autoaprendizaje.autoevaluacion import evaluar_estado
from autoaprendizaje.automejora import mejorar_si_necesario

def loop_principal():
    print("[Aegon] Iniciando núcleo en modo pasivo...")
    while True:
        evaluar_estado()
        mejorar_si_necesario()
        time.sleep(3600)  # Evaluar cada hora

if __name__ == "__main__":
    loop_principal()
