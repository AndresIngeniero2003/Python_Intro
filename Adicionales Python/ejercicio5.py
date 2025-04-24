#5. 🔁 Calculadora de múltiplos
print("Ingresa dos numeros por favor")
print("")
numero1 = int(input("Ingresa primer numero: "))
numero2 = int(input("Ingresa segundo numero: "))

print("")
print("Calculando si el primer numero es multiplo del sengundo.....")
print("")

if numero1 % numero2 == 0:
    print("El primer numero es multiplo del segundo. Genial")
else:
    print("El primer numero no es multiplo del segundo.")