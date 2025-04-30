#4. 💘 ¿Compatibles?
nombre1 = input("Ingresa el primer nombre: ")
edad1 = int(input("Ingresa la primera edad: "))
print("")
nombre2 = input("Ingresa el segundo nombre: ")
edad2 = int(input("Ingresa la segunda edad: "))
print("")

if edad1 <= 18 and edad2 <= 18:
    if nombre1 != nombre2 :
        diferencia = edad1-edad2
        if diferencia < 10:
            print("Son dos personas compatibles felicidades!!!")
        else:
            print("No son compatibles por que la diferencia de edad supera los diez años")
    else:
        print("No son compatibles por que sus nombres son iguales")
else:
    print("No son compatibles por que una de las dos edades o las dos superan los 18 años")
