#  8️⃣ Sistema de préstamos de biblioteca 📚

print("Prestamo de libros")
print("")
cant = int(input("Cantidad de libros prestados -->  "))
sanciones = input("Tienes sanciones pendientes (si/no) -->  ").lower()
print("")

libro = input("Que libro quieres solicitar prestado?  -->   ")
print("")
print("Validando estado..")
print("")

if cant < 3 and sanciones == "no":
    print("Tu libro sera prestado con exito")
else:
    print("No puedes prestar libros conchudote")
    