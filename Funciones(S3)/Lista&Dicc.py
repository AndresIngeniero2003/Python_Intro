# Crea una pequeña agenda en donde se guardara el nombre, el celular, estado civil, genero, todo esto se guardara dentro de un 
# lista para que tengamos una lista de contactos

#     Agregar un nuevo contacto.
#     Buscar un contacto por su nombre o celular.
#     Mostrar todos los contactos.
#     Modificar un contacto en especifico
#     Eliminar un contacto.

# 📦 Requisitos

#     Usar un diccionario para guardar la informacion y dentro de una lista guarda todos estos contactos
#     plus: a la hora de eliminar o modificar que me mustre los contactos existentes para asi verificar cual quiero modificar

lista_contactos = []

#Funciones

def agregar():
    print("Vamos a agregar un nuevo contacto a tu agenda\n")
    nombre = input("Ingresa el nombre:  ").lower()
    celular = input("Ingresa el numero de telefono: ")
    estado = input("Ingresa tu estado civil:  ")
    genero = input("Ingresa tu genero:  ")
    # contactos['nombre'] = nombre
    # contactos['celular'] = celular
    # contactos['estado'] = estado
    # contactos['genero'] = genero
    # lista_contactos.append(contactos)
    
    lista_contactos.append({'nombre':nombre, 'celular':celular, 'estado':estado, 'genero':genero})

    print(lista_contactos)
    
def buscar():
    print("Vamos a buscar en nuestra agenda de contactos un contacto en especifico!\n")
    op = input("Buscar por nombre o por telefono:  ").lower()
    encontrado = False  

    if op == "nombre":
        nombre_buscar = input("Ingresa el nombre del contacto a buscar:  ")
        for contacto in lista_contactos:
            if contacto['nombre'].lower() == nombre_buscar.lower():
                print("\n¡Contacto encontrado!")
                print(f"Nombre: {contacto['nombre']}")
                print(f"Celular: {contacto['celular']}")
                print(f"Estado: {contacto['estado']}")
                print(f"Genero: {contacto['genero']}")
                encontrado = True
                break  
        if not encontrado:
            print("El contacto no se encuentra en la agenda.")

    elif op == "telefono":
        telefono_buscar = input("Ingresa el numero de telefono del contacto a buscar:  ")
        for contacto in lista_contactos:
            if contacto['celular'] == telefono_buscar:
                print("\n¡Contacto encontrado!")
                print(f"Nombre: {contacto['nombre']}")
                print(f"Celular: {contacto['celular']}")
                print(f"Estado: {contacto['estado']}")
                print(f"Genero: {contacto['genero']}")
                encontrado = True
                break  
        if not encontrado:
            print("El contacto no se encuentra en la agenda.")

    else:
        print("Opción de búsqueda no válida. Por favor, elige 'nombre' o 'telefono'.")
                
def eliminar():
    print("Vamos a eliminar un contacto\n")
    nombre_eliminar = input("Ingresa el nombre del contacto a eliminar:  ")
    encontrado = False
    indice_eliminar = -1  

    for i, contacto in enumerate(lista_contactos):
        if contacto['nombre'].lower() == nombre_eliminar.lower():
            indice_eliminar = i
            encontrado = True
            break  

    if encontrado:
        del lista_contactos[indice_eliminar]
        print(f"El contacto '{nombre_eliminar}' ha sido eliminado de la agenda.")
        print(lista_contactos) 
    else:
        print(f"No se encontró ningún contacto con el nombre '{nombre_eliminar}' en la agenda.")
        
def mostrar():    
    cont = 1
    if not lista_contactos:
        print("Lista vacia")
    else:        
        print("Vamos a mostrar la lista de contactos: \n")
        for contacto in lista_contactos:
            print(f"#{cont} Nombre: {contacto['nombre']} Celular: {contacto['celular']} Estado: {contacto['estado']} Genero: {contacto['genero']}")
            cont+=1
        
        
def modificar():
    print("Vamos a modificar un contacto existente en tu agenda\n")
    nombre_buscar = input("Ingresa el nombre del contacto que deseas modificar:  ").lower()
    encontrado = False

    for indice, contacto in enumerate(lista_contactos):
        if contacto['nombre'].lower() == nombre_buscar:
            print("\n¡Contacto encontrado!")
            print(f"Nombre actual: {contacto['nombre']}")
            print(f"Celular actual: {contacto['celular']}")
            print(f"Estado civil actual: {contacto['estado']}")
            print(f"Genero actual: {contacto['genero']}")

            print("\n¿Qué información deseas modificar?")
            print("1. Nombre")
            print("2. Celular")
            print("3. Estado civil")
            print("4. Genero")
            print("5. Modificar todo")
            opcion = input("Ingresa el número de la opción: ")

            if opcion == '1':
                nuevo_nombre = input("Ingresa el nuevo nombre:  ").lower()
                lista_contactos[indice]['nombre'] = nuevo_nombre
                print("Nombre modificado exitosamente.")
            elif opcion == '2':
                nuevo_celular = input("Ingresa el nuevo número de teléfono: ")
                lista_contactos[indice]['celular'] = nuevo_celular
                print("Número de teléfono modificado exitosamente.")
            elif opcion == '3':
                nuevo_estado = input("Ingresa el nuevo estado civil:  ")
                lista_contactos[indice]['estado'] = nuevo_estado
                print("Estado civil modificado exitosamente.")
            elif opcion == '4':
                nuevo_genero = input("Ingresa el nuevo genero:  ")
                lista_contactos[indice]['genero'] = nuevo_genero
                print("Género modificado exitosamente.")
            elif opcion == '5':
                nuevo_nombre = input("Ingresa el nuevo nombre:  ").lower()
                nuevo_celular = input("Ingresa el nuevo número de teléfono: ")
                nuevo_estado = input("Ingresa el nuevo estado civil:  ")
                nuevo_genero = input("Ingresa el nuevo genero:  ")
                lista_contactos[indice]['nombre'] = nuevo_nombre
                lista_contactos[indice]['celular'] = nuevo_celular
                lista_contactos[indice]['estado'] = nuevo_estado
                lista_contactos[indice]['genero'] = nuevo_genero
                print("Información del contacto modificada exitosamente.")
            else:
                print("Opción no válida.")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encontró ningún contacto con el nombre '{nombre_buscar}' en la agenda.")
    

    
    
def menu():
    
    empezar = True
    while empezar:
        opcion = input("""
            Menu principal
            
            1. Agregar contactos
            2. Buscar contacto por nombre o numero de telefono
            3. Eliminar contacto
            4. Mostrar todos los contactos
            5. Modificar un contacto por nombre o telefono
            6. Salir
            opcion -->  """)
        
        match opcion:
            case "1":
                agregar()   
            case "2":
                buscar()
            case "3":
                eliminar()
            case "4":
                mostrar()
            case "5":
                modificar()
            case "6":
                print("\nCerrando agenda virtual..........")
                empezar = False
            case _: 
                print("Opcion incorrecta")

#Estructuracion del problema
print("📒 Mini-Proyecto: Agenda de Contactos\n")
menu()

