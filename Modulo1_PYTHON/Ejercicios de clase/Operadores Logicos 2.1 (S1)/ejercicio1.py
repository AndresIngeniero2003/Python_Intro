#1.Acceso exclusivo al evento
print("Bienvenido al evento mas espectacular del años")
print("")
edad = int(input("Ingresa por favor tu edad: "))
invitacion = int(input("Ingresa tu numero de invitacion: "))

puede_entrar = edad > 21 and invitacion == 777

if puede_entrar:
    print("Puedes ingresar al evento felicidades")
else:
    print("No puedes ingresar")
