#7. Acceso a atracción en parque temático
estatura = float(input("Ingresa tu estatura: "))
edad = int(input("Ingresa tu edad: "))

ingreso = (estatura>140) and (edad > 10) and (edad < 60)

if ingreso:
    print("Puedes ingresar al parque tematico")
else:
    print("No puedes ingresar al parque tematico")

