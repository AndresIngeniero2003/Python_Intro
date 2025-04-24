#1. 📊 Calculadora de promedio con validación

print ("Ingrese tres numero que esten entre 0 y 10")
print ("")
numero1 = int(input("Ingrese el mumero 1: "))
numero2 = int(input("Ingrese el mumero 2: "))
numero3 = int(input("Ingrese el mumero 3: "))

if numero1 < 0 or numero1 > 10 or numero2 < 0 or numero2 > 10 or numero3 < 0 or numero3 > 10: 
    print("Uno de los numeros ingresados esta fuera de rango")
else:
    total = numero3 + numero2 + numero1
    promedio = total/3
    if promedio>=6:
        print("El estudiante APROBO")
    else:
        print("El estudiante REPROBO")
        