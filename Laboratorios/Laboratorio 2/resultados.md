# Resultados

## Método de concurrencia elegido: Concurrencia basada en hilos

**Razón de elección:** Elegimos la concurrencia basada en hilos debido a que el problema está relacionado con operaciones de I/O (consultas a una API remota). Al usar hilos, podemos realizar múltiples consultas en paralelo, aprovechando mejor el tiempo de espera de la respuesta del servidor.

## Rendimiento

**Versión sin concurrencia:** Tiempo total = 31.93165135383606 seconds

**Versión con concurrencia:** Tiempo total = 2.7622478008270264 seconds

Comparando los resultados, observamos que la implementación con concurrencia basada en hilos mejora significativamente el rendimiento en comparación con la versión sin concurrencia. La diferencia en el tiempo de ejecución es notable, lo que demuestra la eficacia de la concurrencia para realizar operaciones I/O bound de manera más eficiente.
