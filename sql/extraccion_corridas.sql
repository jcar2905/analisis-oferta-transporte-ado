-- Extracción de corridas 2024 para anlisis de la oferta
-- Base de datos: ado_db | Tabla: corridas
-- Ejecutado por Juan Carlos Haro Ortega | 2026

SELECT id_corrida,
fecha,
dia_semana,
horario_salida,
ruta,
terminal_origen,
tipo_unidad,
capacidad,
pasajeros,
ocupación_pct,
precio_boleto,
ingresos_totales,
temporda
FROM corridas
WHERE fecha BETWEEN '2024-01-01'  AND '2024-12-31'
ORDER BY fecha, ruta, horario_salida