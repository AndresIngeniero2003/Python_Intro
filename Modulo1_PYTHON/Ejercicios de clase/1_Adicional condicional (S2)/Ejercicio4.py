# 🔹 4️⃣ Calculadora de presupuesto mensual 💰

print("Calculadora de presupuesto mensual")
print("")

ingresos = float(input("Ingresa tus ingresos mensuales -->  "))
gastos = float(input("Ingresa el total de tus gastos fijos -->  "))

if ingresos>gastos:
    ahorro = ingresos-gastos
    print("Tus gastos no superan tus ingresos felicidades!")
    print("Tienes para ahorrar: ", ahorro)
    print("")
else:
    print("Cuidado tus gastos son superiores a tus ingresos")