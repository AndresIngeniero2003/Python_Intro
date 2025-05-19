# 🔹 9️⃣ Asistente de compras inteligentes 🛍️
# Crea un sistema que ayude al usuario a decidir si comprar un producto.
# Pide:
print("Asistente de compras inteligentes 🛍️")
print("")
precio = float(input("Ingresa el precio del producto -->  "))
opc = input("Hay descuento(si/no) -->  ").lower()
des = 0
if opc == "si":
    des = int(input("Ingresa el valor del descuento -->  "))
    des = precio - (precio*des/100)
    precio = precio - des
presupuesto = float(input("De cuanto es tu presupuesto de compras  -->  "))
print("")
if precio>presupuesto:
    print("La compra no es recomendable ya el precio es mayor al presupuesto")
else:
    print("Compra recomendada puedes hacerla")