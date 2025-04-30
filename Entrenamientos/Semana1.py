#Entrenamiento semana #1 calcular el costo total de una compra
print("Calcularemos el costo total de una compra hecha..........")
print("")

#solicitar por consola cuatro datos
nombre_pro = input("¿Cual es el nombre del producto?: ")
precio_uni = float(input("¿Cual es el precio del producto?: "))
cantidad = int(input("¿Que cantidad llevas?: "))
porcentaje = int(input("¿Cual es el porcentaje de descuento del producto?(0% -> 100%): "))
print("")

#Validaciones 
#Precio y cantidan deben ser valores positivos y el porcentaje debe estar dentro del rango (0% -> 100%)
print("Validando precio, cantidad y porcentaje..........")
print("")

if precio_uni > 0:
    print("El precio es correcto!")
    if cantidad > 0:
        print("La cantidad es correcta!")
        if porcentaje >= 0 and porcentaje <= 100:
            print("Porcentaje dentro del rango !!")
            print("")
            #Salidas
            costo_bruto = precio_uni * cantidad
            costo_neto = costo_bruto - costo_bruto*porcentaje/100
            print(f"El nombre del producto es {nombre_pro} y el costo neto de la compa es: {costo_neto:.2f} ")
        elif porcentaje == 0:
            print(f"El producto {nombre_pro} no tiene descuento")
            print("")
            print("Programa terminado!")
        else:
            print("El porcentaje ingresado no esta dentro del rango X")
    else:
        print("La cantidad ingresada es incorrecta X")
else:
    print("El precio es incorrecto X")

