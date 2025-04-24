#9. Evaluación para tarjeta de crédito
ingresos = float(input("Ingresos mensuales: "))
deudas = input("Tienes deudas activos (si o no):")

if ingresos>2500:
    print("Puedes recibir tarjeta")
elif (ingresos > 1500) and (deudas.lower() == "no"):
    print("Puedes recibir tarjeta")
else:
    print("No puedes recibir tarjeta")


