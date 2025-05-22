# 🔹 6️⃣ Sistema de registro de eventos con validación 🎟️

print("Evento del año fantastico: solo quedan 3 cupos")
cupo = 3
bandera = True
while bandera:
    nombre = (input("Ingresa tu nombre -->  "))
    edad = int(input("Ingresa tu edad -->  "))
    print("")
    print("Validando cupo.")
    print("")
    if edad>15:
        if cupo > 0:
            print("Puedes ingresar al evento. Felicidades!")
            cupo = cupo - 1
        else:
            print("No quedan cupos")
            bandera = False
    else:
        print("No tienes la edad suficiente para ingresar al evento")
