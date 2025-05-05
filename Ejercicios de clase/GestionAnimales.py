def agregar(nombre, edad, enfermo):
    global lista_Nombre
    global lista_Edad
    global lista_Enfermo
    lista_Nombre.append(nombre)
    lista_Edad.append(edad)
    lista_Enfermo.append(enfermo)
    print(f"Pacientes agregados: {lista_Nombre}")
    
def eliminar(nombre):
    global lista_Nombre
    global lista_Edad
    global lista_Enfermo
    encontrado = False
    indice = 0
    for elemento in lista_Nombre:
        if nombre == elemento:
            encontrado = True
            indice = lista_Nombre.index(elemento)
            break
        
    if encontrado:
        print("La mascota se encuentra en nuestra base de datos, perfecto! ELIMINANDO.......    ")           
        del lista_Nombre[indice]
        del lista_Edad[indice]
        del lista_Enfermo[indice]
    else:
        print("La mascota no fue encontrada en nuestra base de datos")
        
    print(lista_Nombre, lista_Edad, lista_Enfermo)
    
def listar():
    global lista_Nombre
    global lista_Edad
    global lista_Enfermo
    longitud = len(lista_Nombre)
    lista_estado = []
    for elemento in lista_Enfermo:
        if elemento == "si":
            lista_estado.append("enferm@")
        else:
            lista_estado.append("san@")
    for i in range(longitud):
        N = lista_Nombre[i]
        E = lista_Edad[i]
        Es = lista_estado[i]
        print(f"La mascota {N} tiene {E} (años o meses) y esta {Es} ")
        

print("**********<Gestion de animales>**********\n")

#Variables globales
lista_Nombre = []
lista_Edad = []
lista_Enfermo = []


#Estructuracion
print("Iniciando software...\n")

iniciar = True

while iniciar:
    opcion = int(input("""
        **********<Menu principal>**********
        
            1. Agregar mascota
            2. Eliminar mascota
            3. Ver base de datos
            4. Salir
            ingresa la opcion -->  """))

    match opcion:
            case 1:
                print("Haz seleccionado la opcion agregar, cargando..........\n")
                nombre = input("Ingresa el nombre de la mascota:  ").lower()
                edad = int(input("Ingresa la edad de la mascota:  "))
                enfermo = input("¿Tu mascota esta enferma(si/no):  ").lower()
                agregar(nombre,edad,enfermo)          
            case 2:
                print("Haz seleccionado la opcion eliminar, cargando..........\n")
                nombre = input("Ingresa el nombre de la mascota:  ")
                eliminar(nombre)
            case 3:
                print("Haz seleccionado la opcion listar, cargando..........\n")
                listar()
            case 4:
                print("Cerrando software..........")
                iniciar = False
            case _:
                print("Opcion incorrecta cerrando software..........\n")
                iniciar = False

            