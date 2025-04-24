#6. 🧠 Número mágico
numero = int(input("Ingresa un numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 5 == 0:
        print("Buzz")
elif numero % 3 == 0:
        print("Frizz")
else:
        print("Nada magico")