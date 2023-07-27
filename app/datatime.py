import random
from datetime import datetime, timedelta
"""
Esto lo use para Generar fechas aleatorias
"""
def generar_fecha_hora_aleatoria():
    fecha_actual = datetime.now()
    dias_aleatorios = random.randint(1, 365)
    horas_aleatorias = random.randint(0, 23)
    minutos_aleatorios = random.randint(0, 59)
    segundos_aleatorios = random.randint(0, 59)
    fecha_hora_aleatoria = fecha_actual + timedelta(days=dias_aleatorios, 
                                                    hours=horas_aleatorias,
                                                    minutes=minutos_aleatorios,
                                                    seconds=segundos_aleatorios)
    
    return fecha_hora_aleatoria

# Ejemplo de uso:
for _ in range(140):
    fecha_hora = generar_fecha_hora_aleatoria()
    print(fecha_hora)