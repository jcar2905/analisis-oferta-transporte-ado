# analisis-oferta-transporte-ado

## Descripción
Pipeline completo de análisis de datos: extracción SQL, limpieza con Python, análisis exploratorio y dashboard en Power BI. Dataset de 2,500 corridas de autobús.

## Objetivo
Identificar rutas y horarios con excesos de oferta y demanda insatisfecha para apoyar decisiones comerciales de asignación de unidades.

## Pipeline de datos

** SQL -> Python -> Power BI**

1. Extracción de datos históricos de corridas con SQL
2. Limpieza y transformación con Python (pandas)
3. Análisis exploratorio y visualización
4. Dashboard interactivo en Power BI

## Hallazgos principales

| Hallazgo | Detalle |
|---|---|
| Ocupación promedio global | 74.5% — dentro del rango óptimo (70-85%) |
| Fin de semana vs entre semana | 87.6% vs 69.2% — diferencia de 18 puntos |
| Demanda insatisfecha | 11 horarios con 100% de ocupación en fin de semana |
| Exceso de oferta crítico | CDMX-Tlaxcala 21:00 entre semana: 47.6% |
| Ruta más rentable | CDMX-Querétaro — $5.4M en ingresos anuales |

## Recomendaciones
- Reducir frecuencias entre semana en horario valle (12-16hrs) en rutas con ocupación <60%
- Aumentar frecuencias los fines de semana en horarios con ocupación >90%
- Priorizar unidades de mayor capacidad en CDMX-Querétaro fines de semana

## Estructura del repositorio

- **data/** — Dataset simulado de 2,500 corridas y script generador
- **sql/** — Consulta de extracción desde base de datos relacional
- **notebooks/** — Jupyter Notebook con limpieza y análisis completo
- **visualizations/** — Gráficas generadas del análisis
- **powerbi/** — Dashboard interactivo con 3 páginas

## Tecnologías

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)

## Nota sobre los datos
El dataset es simulado con fines educativos y de práctica. 
Incluye problemas de calidad reales: fechas en múltiples formatos, 
nombres inconsistentes, nulos, duplicados y outliers.

## Autor
**Juan Carlos Haro Ortega**  
Licenciado en Matemáticas Aplicadas — UAEH 2025  
carloshaor@outlook.com | [github.com/jcar2905](https://github.com/jcar2905)
