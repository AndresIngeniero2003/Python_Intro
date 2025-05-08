#store product inventory  --- EJERCICIO HECHO CON LISTAS QUE CONTIENEN DICCIONARIOS Y A SU VEZ ESTOS CONTIENEN DUPLAS

#global variable
# list_product = []
dicc_productos = {}
list_product = []

#functions
def menu():
    
    init = True
    while init:
        option = (input("""
                        **********<Menu principal>**********
                        
                        1. Añadir productos
                        2. Consultar productos
                        3. Actualizar productos
                        4. Eliminar productos
                        5. Calcular total del inventario
                        6. Salir
                        opcion -->  """))
        if option.isdigit(): 
            rank = int(option)
            if 1 <= rank <= 6:
                match rank:
                    case 1:
                        print("\nVamos a añadir un nuevo producto!\n")
                        name = input("Ingresa el nombre del producto:  ").lower().strip()
                        while True:
                            try:
                                price = float(input("Ingresa el precio del producto:  "))
                                if price >= 0:
                                    break 
                                else:
                                    print("El precio no puede ser negativo")
                            except:
                                print("Entrada incorrecta para el precio, ingresa un número\n")

                        while True:
                            try:
                                quantity = int(input("Ingresa la cantidad del producto:  "))
                                if quantity >= 0:
                                    break 
                                else:
                                    print("La cantidad no puede ser negativa\n")
                            except:
                                print("Entrada incorrecta para la cantidad, ingresa un número entero.\n")
        
                        add_product(name, price, quantity)
                    case 2:
                        print("\nVamos a consultar un producto\n")
                        name = input("Ingresa el nombre del producto:  ").lower().strip()
                        tupla_datos = consult_product(name)
                        if not tupla_datos:
                            print("El producto no esta en la base de datos")
                        else:
                            print(f"\nNombre: {name}\nPrecio: {tupla_datos[0]}\nCantidad: {tupla_datos[1]}")                            
                    case 3:
                        print("\nVamos a actualizar el precio de un producto\n")
                        name = input("Ingresa el nombre del producto:  ").lower().strip()
                        while True:
                            try:
                                price = float(input("Ingresa el precio del producto:  "))
                                if price >= 0:
                                    break 
                                else:
                                    print("El precio no puede ser negativo")
                            except:
                                print("Entrada incorrecta para el precio, ingresa un número\n")
                        
                        update_product(name, price)
                    case 4:
                        print("\nVamos a eliminar un producto\n")
                        delete_product()
                    case 5:
                        print("\nVamos a calcular el total del inventario\n")
                        inventory_total()
                    case 6:
                        print("\nCerrando software..........\n")
                        init = False
            else:
                print("\nEstas fuera del rango 1-6")
        else: 
            print("\nNo puedes ingresar letras, recuerda solo numeros")
        
def add_product(name, price, quantity):
    validate = False
    for product in list_product:
        if name in product:
            validate = True
            break
    if validate == False:
        list_product.append({name : (price, quantity)})
    else:
        print("El producto ya esta en la base de datos\n")
        
    print(list_product)
    
def consult_product(name):
    for product in list_product:
        if name in product:
            price, quantity = product[name]
            return price, quantity  
    
def update_product(name, price):
    validate = False
    for product in list_product:
        if name in product:
            cant = product[name][1]
            product[name] = (price,cant)
            validate = True
            print(f"\nNombre: {name} \nPrecio actualizado: {product[name][0]}")
    if not validate :
        print(f"El profucto {name} no se enceuntra")

def delete_product():
    print
    
def inventory_total():
    print

#program start
print("Iniciando software de inventarios..........\n")
print("Software iniciado correctamente.\n")
menu()

