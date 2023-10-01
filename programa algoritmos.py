Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Marjory Berganza/AppData/Local/Programs/Python/Python311/pythonexerci.py
Bienvenido al programa para llevar un registro de sus tareas.
Menú de opciones:
1. Agregar una tarea
2. Listar tareas pendientes
3. Listar tareas completadas
4. Marcar tarea como completada
5. Salir
Ingrese el número de la opción que quiere elegir: 1
Ingrese el título de la tarea: tarea mate discreta
Ingrese la descripción de la tarea: proyecto final
Ingrese la fecha de vencimiento de la tarea (opcional): 01/10/2023
Traceback (most recent call last):
  File "C:/Users/Marjory Berganza/AppData/Local/Programs/Python/Python311/pythonexerci.py", line 139, in <module>
    agregar_tarea(tareas_pendientes)
  File "C:/Users/Marjory Berganza/AppData/Local/Programs/Python/Python311/pythonexerci.py", line 64, in agregar_tarea
    tarea = Tarea(titulo, descripcion, fecha)
TypeError: Tarea() takes no arguments
