"""
Dataset simulado de corridas ADO 2024
Generado con fines educativos y de práctica de análisis de datos
Autor: Juan Carlos Haro Ortega
"""

import pandas as pd
import numpy as np 
import random

np.random.seed(42)
random.seed(42)

rutas_sucias = [
    "CDMX-Puebla", "cdmx - puebla", "CDMX - Puebla",
    "CDMX-Querétaro", "CDMX-Queretaro", "cdmx-queretaro",
    "CDMX-Toluca", "CDMX - Toluca",
    "CDMX-Cuernavaca", "CDMX-cuernavaca",
    "CDMX-Pachuca", "CDMX - Pachuca",
    "CDMX-Tlaxcala"
]

horarios = ["06:00","07:00","08:00","09:00","10:00","11:00",
            "12:00","13:00","14:00","15:00","16:00","17:00",
            "18:00","19:00","20:00","21:00","22:00"]

tipos_unidad = ["Ejecutivo","Primera Plus","ADO GL","OCC"]

terminales     = ["TAPO","Poniente","Norte","Sur","Observatorio"]
capacidad_dict = {"Ejecutivo":24,"Primera Plus":36,"ADO GL":48,"OCC":42}
precio_base    = {
    "CDMX-Puebla":280,"cdmx - puebla":280,"CDMX - Puebla":280,
    "CDMX-Querétaro":320,"CDMX-Queretaro":320,"cdmx-queretaro":320,
    "CDMX-Toluca":180,"CDMX - Toluca":180,
    "CDMX-Cuernavaca":220,"CDMX-cuernavaca":220,
    "CDMX-Pachuca":190,"CDMX - Pachuca":190,
    "CDMX-Tlaxcala":240
}

from datetime import datetime, timedelta
fecha_inicio = datetime(2024, 1, 1)
registros = []

for i in range(2500):
    fecha      = fecha_inicio + timedelta(days=random.randint(0, 364))
    dia_semana = fecha.weekday()
    ruta       = random.choice(rutas_sucias)
    horario    = random.choice(horarios)
    tipo       = random.choice(tipos_unidad)
    terminal   = random.choice(terminales)
    capacidad  = capacidad_dict[tipo]
    hora       = int(horario.split(":")[0])

    ocupacion_base = 0.65
    if dia_semana >= 5:        ocupacion_base += 0.20
    if hora in [7,8,9,17,18,19]: ocupacion_base += 0.15
    ocupacion_base = min(ocupacion_base, 1.0)

    pasajeros  = int(capacidad * np.random.normal(ocupacion_base, 0.12))
    pasajeros  = max(0, min(pasajeros, capacidad))
    precio     = precio_base.get(ruta, 250) * (1 + random.choice([0,0,0,0.10,0.20,-0.05]))
    ingresos   = round(pasajeros * precio, 2)
    ocupacion  = round((pasajeros / capacidad) * 100, 1)

    formatos = [fecha.strftime("%Y-%m-%d"), fecha.strftime("%d/%m/%Y"),
                fecha.strftime("%d-%m-%Y"),  fecha.strftime("%Y/%m/%d")]
    fecha_str = random.choices(formatos, weights=[0.6,0.2,0.1,0.1])[0]

    registros.append({
        "id_corrida": f"ADO-{str(i+1).zfill(5)}",
        "fecha": fecha_str, "dia_semana": fecha.strftime("%A"),
        "horario_salida": horario, "ruta": ruta,
        "terminal_origen": terminal, "tipo_unidad": tipo,
        "capacidad": capacidad, "pasajeros": pasajeros,
        "ocupacion_pct": ocupacion, "precio_boleto": round(precio,2),
        "ingresos_totales": ingresos,
        "temporada": "Alta" if fecha.month in [12,1,7,8] else "Baja"
    })

df = pd.DataFrame(registros)

# Introducir problemas de calidad realistas
df.loc[df.sample(frac=0.05).index, "pasajeros"]        = np.nan
df.loc[df.sample(frac=0.04).index, "ingresos_totales"] = np.nan
df.loc[df.sample(frac=0.03).index, "tipo_unidad"]      = np.nan
df.loc[df.sample(n=15).index, "ingresos_totales"]      *= -1
df.loc[df.sample(n=10).index, "pasajeros"]             *= 1.3
df = pd.concat([df, df.sample(n=20)], ignore_index=True)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv("data/dataset_ADO_corridas.csv", index=False, encoding="utf-8-sig")
print(f"Dataset generado: {len(df)} registros")