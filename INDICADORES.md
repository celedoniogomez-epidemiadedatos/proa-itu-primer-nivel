# Indicadores PROA-ITU

Seis indicadores para dar seguimiento a la prescripción en cistitis aguda no complicada. Corresponden al elemento de **seguimiento y reporte** del marco de optimización de antimicrobianos en atención ambulatoria de los CDC (ver [FUENTES.md](FUENTES.md)). Las definiciones y las metas son **propuestas de trabajo**: cada institución debe ajustarlas.

Las columnas del archivo [datos_simulados.csv](datos_simulados.csv) corresponden a los numeradores y denominadores de abajo.

| N.º | Indicador | Numerador | Denominador | Meta de ejemplo |
|---|---|---|---|---|
| I1 | Uso de esquema de primera línea | Consultas con esquema recomendado (`esquema_primera_linea`) | Consultas por cistitis no complicada (`consultas_cistitis_nc`) | 80 % o más |
| I2 | Duración adecuada del tratamiento | Consultas con duración adecuada al esquema (`duracion_adecuada`) | Consultas por cistitis no complicada | 90 % o más |
| I3 | Uso de fluoroquinolonas | Consultas con fluoroquinolona (`fluoroquinolona`) | Consultas por cistitis no complicada | 10 % o menos |
| I4 | Urocultivo cuando está indicado | Urocultivos realizados (`urocultivo_realizado`) | Casos con indicación de urocultivo (`urocultivo_indicado`) | 80 % o más |
| I5 | Reconsulta a los 14 días | Pacientes que reconsultan por el mismo motivo (`reconsulta_14d`) | Consultas por cistitis no complicada | Vigilar tendencia; no hay meta universal |
| I6 | Bacteriuria asintomática tratada | Casos tratados (`bacteriuria_asintomatica_tratada`) | Casos detectados (`bacteriuria_asintomatica_detectada`) | Lo más cercano a 0 % (excepto embarazo y procedimiento urológico) |

## Cómo interpretarlos

- **I1, I2 e I3** miden si se sigue la guía. Si I1 sube y I3 baja, el programa está funcionando.
- **I4** controla que no se trate a ciegas cuando hay motivo para cultivar.
- **I5** es un indicador de **seguridad**: si I1 mejora pero I5 empeora, puede estar fallando el tratamiento. Conviene revisar antes de seguir presionando la prescripción.
- **I6** evita el sobretratamiento de bacteriuria asintomática, uno de los errores más frecuentes.

## Recomendaciones de captura

- Define un criterio único de "cistitis no complicada" para todo el equipo (ver el paso 1 del [algoritmo](ALGORITMO.md)).
- Registra los datos por unidad y por mes, sin datos personales del paciente.
- Reporta resultados a cada unidad y compáralos con su propio historial antes de compararlos con otras unidades.
- Revisa las metas cada 6 a 12 meses con el equipo.

*Del dato al cuidado.*
