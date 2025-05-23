#store product inventory  --- EJERCICIO HECHO CON LISTAS QUE CONTIENEN DICCIONARIOS Y A SU VEZ ESTOS CONTIENEN DUPLAS

#global variable
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
        if option.isdecimal():       #Valido que solo me ingresen numero, si el metodo retorna true entra al codigo 
            rank = int(option)        #si no se sale y notifica de manera amigable que solo debe ingresar numero
            if 1 <= rank <= 6:
                match rank:         #Valido que este dentro del rango de opciones 
                    case 1:
                        print("\nVamos a añadir un nuevo producto!\n")
                        name = input("Ingresa el nombre del producto:  ").lower().strip()
                        while True:
                            str_price = input("Ingresa el precio del producto:  ")
                            if str_price.isdecimal():
                                price = float(str_price)
                                if price >= 0:             #Valido que sea un numero positivo y que en la variable precios solo se ingresen numeros
                                    break 
                                else:
                                    print("El precio no puede ser negativo")
                            else:
                                print("Solo puedes ingresar numeros\n")
                        while True:
                            str_quantity = input("Ingresa la cantidad del producto:  ")
                            if str_quantity.isdecimal():
                                quantity = int(str_quantity)
                                if quantity >= 0:               #Mismo proceso valido que los valores sean positivos y solo se ingresen numeros
                                    break 
                                else:
                                    print("La cantidad no puede ser negativa\n")
                            else:
                                print("Solo puedes ingresar numeros\n")                                    
                        add_product(name, price, quantity)                          #Envio por variables capturadas como argumentos a la funcion
                    case 2:
                        print("\nVamos a consultar un producto\n")
                        name = input("Ingresa el nombre del producto:  ").lower().strip()   #Metodos usados para convertir cadena de texto en minusculas y
                        tupla_datos = consult_product(name)                                 #eliminar espacios al final y al inicio
                        if not tupla_datos:      #Si la tupla esta vacia es porque no se encontro registro del producto buscado
                            print("El producto no esta en la base de datos")
                        else:
                            print(f"\nNombre: {name}\nPrecio: {tupla_datos[0]}\nCantidad: {tupla_datos[1]}")                            
                    case 3:
                        print("\nVamos a actualizar el precio de un producto\n")
                        name = input("Ingresa el nombre del producto:  ").lower().strip()
                        while True:
                            str_price = input("Ingresa el precio del producto:  ")
                            if str_price.isdecimal():
                                price = float(str_price)
                                if price >= 0:
                                    break 
                                else:
                                    print("El precio no puede ser negativo")
                            else:
                                print("Solo puedes ingresar numeros\n")                        
                        update_product(name, price)
                    case 4:
                        print("\nVamos a eliminar un producto\n")
                        name = input("Ingresa el nombre del producto:  ").lower().strip()
                        delete_product(name)
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


def add_product(name, price, quantity): #recibo variables como parametros 
    validate = False                #variable usada para marcar si se encuentra o no el producto
    for product in list_product:
        if name in product:
            validate = True
            break
    if validate == False:               #Si el producto no se encuenta agregar de manera exitosa
        list_product.append({name : (price, quantity)})
    else:
        print("El producto ya esta en la base de datos\n")       #Si la vairable cambia su valor booleano a True indica que el producto ya esta agregado
        
    print(list_product)             #Imprimo lista para verificar que se esten agregando valores correctamente
    
def consult_product(name):
    for product in list_product:
        if name in product:
            price, quantity = product[name]     #Si encuentro considencias dentro del diccionario que esta dentro de la lista capturo su precio y la cantida almacenados en una tupla
            return price, quantity              #Retorno los valores para ser imprimidos desde el menu
    
def update_product(name, price):
    validate = False
    for product in list_product:
        if name in product:
            cant = product[name][1]         #Las tuplas son inmutables debo capturar la cantidad de producto para no perder el valor y asi 
            product[name] = (price,cant)    #reescribri la tupla dentro de la lista con el precio nuevo
            validate = True
            print(f"\nNombre: {name} \nPrecio actualizado: {product[name][0]}")
    if not validate :
        print(f"El producto {name} no se encuentra")            #Valido afuera del for para evitar que en las iteraciones donde el name no sea igual 
                                                            #Se me este impriemiendo el mensaje sobre que el producto no se encuentra
def delete_product(name):
    validate = False
    indice = -1
    for i, product in enumerate(list_product):          #Este metodo enumerate me devuelve el indice del lugar donde estoy y lo que hay en el
        if name in product:
            indice = i                      #Capturo el indice para eliminar el producto fuera del for para no tener errores por longitud
            validate = True
            break                           #Una vez encuentro el producto con el break rompo el codigo ya que no es necesario mas iteraciones
    if not validate :
        print(f"El producto {name} no se encuentra")
    else:
        del list_product[indice]
    
def inventory_total():
    total_producto = lambda item: list(item.values())[0][0] * list(item.values())[0][1]
                                                                #mi funcion lambda accede a los elementos de la tupla convirtiendolos en listas
    valores_productos = map(total_producto, list_product)      #y accediendo a ellos mediente su indice para asi operar y calcular su valor
    total_inventario = sum(valores_productos)                   
                                                            #Los metodos anteriores se usan para que mi funcion lambda repita el procedimiento con todos los valores de la lista
    print(f"El valor total del inventario es: ${total_inventario}")

#program start
print("Iniciando software de inventarios..........\n")
print("Software iniciado correctamente.\n")
menu()

