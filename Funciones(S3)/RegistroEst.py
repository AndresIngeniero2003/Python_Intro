# Ejercicio 1: Registro de Estudiantes
# Objetivo:

# Crear un diccionario para almacenar información sobre estudiantes y realizar algunas 
# operaciones básicas como agregar, modificar y mostrar datos.
# Instrucciones:

# Crea un diccionario llamado estudiantes, donde las claves sean los nombres de los estudiantes y los valores sean otro diccionario 
# con las claves edad y calificacion.

#     El programa debe permitir al usuario realizar las siguientes operaciones:
#         Agregar un nuevo estudiante (nombre, edad, calificación).
#         Modificar la calificación de un estudiante.
#         Mostrar la información de todos los estudiantes.
#         Eliminar un estudiante por su nombre.

#Funciones

    

print("Registro de estudiantes\n")
menu = True
while menu:
    opcion = input(
        """Menu de registro RIWI
                    
        1. Agregar coder
        2. Modificar calificacion de un coder
        3. Mostrar todos los coders
        4. Eliminar un coder
        Seleccion -->  """)
    
    match opcion:
            case "1":
                agregar()   
            case "2":
                buscar()
            case "3":
                eliminar()
            case "4":
                print("\nCerrando agenda virtual..........")
                menu = False
            case _: 
                print("Opcion incorrecta")
    

