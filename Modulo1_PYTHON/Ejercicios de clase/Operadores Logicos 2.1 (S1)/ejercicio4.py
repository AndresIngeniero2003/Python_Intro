#4. Evaluación académica de estudiante
n1 = int(input("ingresa primera nota: "))
n2 = int(input("ingresa segunda nota: "))

aprobo = (n1>=6 and n2>=6) and (n1>4 and n2>4)

if aprobo:
    print("Apruebas")
else:
    print("No aprobaste")
