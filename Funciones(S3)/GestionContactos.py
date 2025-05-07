diccionario = {}

def menu():
    
    empezar = True
    while empezar:
        opcion = input("""
            Menu principal
            
            1. Agregar contactos
            2. Buscar contacto
            3. Eliminar contacto
            4. Mostrar todos los contactos
            5. Salir
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
                print("\nCerrando agenda virtual..........")
                empezar = False
            case _: 
                print("Opcion incorrecta")
                
def agregar():
    print("Vamos a crear un nuevo contacto\n")
    nombre = input("Ingresa el nombre:  ").lower()
    if nombre in diccionario:
        print("El contacto ya esta en tu lista\n")
    else:
        telefono = input("Ingresa el numero de telefono:  ").strip()
        diccionario[nombre] = telefono
        
def buscar():
    nombre = input("Ingresa el nombre del contacto a buscar:  ")
    if nombre in diccionario:
        print("El nombre se encuenta en tu lista de contactos")
        print(f"Nombre -> {nombre} Telefono -> {diccionario[nombre]} ")
    else:
        print("No se encontro el nombre en tu lista de contactos\n")
        
def eliminar():
    nombre = input("Ingresa el nombre del contacto a eliminar:  ")
    if nombre in diccionario:
        del diccionario[nombre]
    else:
        print("El contacto no existe")
    
def mostrar():
    print("Vamos a mostar todos tus contactos\n")
    if not diccionario:
        print("Tu lista de contactos esta vacia")
    else:
        for nombre, telefono in diccionario.items()   :
            print(f"Nombre: {nombre} Telefono: {telefono}\n")
        
    

inicio = True

if inicio:
    print("Bienvenido a tu agenda virtual de contactos")
    menu()
