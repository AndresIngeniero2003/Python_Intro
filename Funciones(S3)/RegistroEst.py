
#Diccionario global
dicc_Estudiantes = {}

#Funciones
def agregar ():
    print("\nVamos a agregar un nuevo coder!")
    nombre = input("Ingresa el nombre del coder:  ")
    edad = int(input("Ingresa la edad del coder:  "))
    calificacion = float(input("Ingresa la calificacion del  coder(0 ->100):  "))
    dicc_Estudiantes[nombre] = {"edad" : edad, "calificacion" : calificacion}
    print(dicc_Estudiantes)
    

def modificar_cal():
    print("\nVamos a modificar la calificacion de un coder!")
    nombre = input("Ingresa el nombre del coder:  ")
    if nombre in dicc_Estudiantes:
        nuevaCalificacion = float(input("Ingresa la nueva calificacion para actualizarla:  "))
        dicc_Estudiantes[nombre]["calificacion"] = nuevaCalificacion
        print(f"La calificación de {nombre} ha sido actualizada a {nuevaCalificacion}")
        print(dicc_Estudiantes)
    else:
        print(f"No se encontró ningún coder con el nombre '{nombre}'.")
        
def mostrar():
    for nombre in dicc_Estudiantes:
        datos = dicc_Estudiantes[nombre]
        print(f"\nNombre: {nombre} Edad: {datos['edad']} Calificacion: {datos['calificacion']}\n")
        
    # for n, d in dicc_Estudiantes.items():
    #     print(f"Nombre: {n} Edad: {d['edad']} Calificacion: {d['calificacion']}")
    
def eliminar():
    print("Vamos a eliminar un coder\n")
    nombre = input("Ingresa el nombre del coder:  ")
    del dicc_Estudiantes[nombre]
    print(dicc_Estudiantes)
    
    

#Estructura del problema
print("Registro de coders\n")
menu = True
while menu:
    opcion = input(
        """Menu de registro RIWI
                    
        1. Agregar coder
        2. Modificar calificacion de un coder
        3. Mostrar todos los coders
        4. Eliminar un coder
        5. Salir
        Seleccion -->  """)
    
    match opcion:
            case "1":
                agregar()   
            case "2":
                modificar_cal()
            case "3":
                mostrar()
            case "4":
                eliminar()
            case "5":
                print("\nCerrando agenda virtual..........")
                menu = False
            case _: 
                print("Opcion incorrecta")
    

