#4. 💘 ¿Compatibles?
nombre1 = input("Ingresa el primer nombre: ")
edad1 = int(input("Ingresa la primera edad: "))
print("")
nombre2 = input("Ingresa el segundo nombre: ")
edad2 = int(input("Ingresa la segunda edad: "))
print("")

if (edad1 and edad2 <= 18) and (nombre1 and nombre2 == "rótulos"):
    diferencia = edad1-edad2
    if diferencia > 10:
        print("No son compatibles por que su diferencia de edad supera los 10 años")
    else:
        print("Son dos personas compatibles felicidades!!!!")
elif edad1 or edad2 > 18:
    print("No son compatibles por que uno de los dos es mayor de 18 años")
else:
    print("No son compatibles por que ambos no se llaman rótulos")




# Pide:

# Nombre y edad de dos personas
# Verifica si:

# Ambos tienen al menos 18 años.
# Se llaman rótulos
# La diferencia de edad no supera los 10 años.
# Si cumple todo, imprime un mensaje gracioso diciendo que son compatibles 💞
# Si no, di por qué no lo son .