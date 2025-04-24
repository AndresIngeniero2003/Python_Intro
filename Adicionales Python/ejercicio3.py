#3. 🧮 Calculadora de salario neto
sueldo_b = float(input("Ingresa por favor tu suelo: "))
descuento = int(input("Ingresa tu porcentaje de descuento: "))

sueldo_n = sueldo_b - (sueldo_b * descuento / 100)
print("")
print("Tu sueldo bruto es de: ", sueldo_b, " Tu descuento es de: ", descuento, "% Tu sueldo neto es de: ", sueldo_n)
