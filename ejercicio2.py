#2. ⏳ Años para jubilarse
Edad = int(input("Ingresa por favor tu edad: "))
Genero = input("Ingresa por favor tu genero(M->mujer o H->hombre: ")

if Genero.lower() == "m":
    if Edad == 60:
        print("Felicidades ya puedes jubilarte")
    elif Edad > 60:
        print("Ya estas jubilada")
    else:
        faltante = 60-Edad
        print("Te faltan ",faltante," años para jubilarte. MUJER")
elif Genero.lower() == "h":
    if Edad == 65:
        print("Felicidades ya puedes jubilarte")
    elif Edad > 65:
        print("Ya estas jubilado")
    else:
        faltante = 65-Edad
        print("Te faltan ",faltante," años para jubilarte. HOMBRE")
else:
    print("Genero ingresado de manera incorrecta")
