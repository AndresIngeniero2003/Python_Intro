#2. Descuento por edad o monto
monto = float (input("ingresa el monto total de tu compra: "))
edad = int(input("ingresa tu edad: "))

descuento = monto>100 or edad > 60

if descuento:
    print("Obtines un descuento. Genial")
else:
    print("No puedo darte descuento.")

