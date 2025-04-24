#Entrada al clud unicornio ninja
Edad = int (input("Ingresa tu edad por favor: "))
if Edad>=18:
    PaseDorado = input("¿Tienes pase dorado? (Si-No): ")
    if PaseDorado == "si":
        print("Puedes ingresar al clud. FELICIDADES!!")
    elif Edad <= 25:
        print("Puedes ingresar al clud. FELICIDADES!!")
    else:
        print("Eres mayor de 25 años y no tienes pase dorado")
        print("Acceso DENEGADO!")
else:
    print("Eres menor de edad")
    print("No puedes entrar al clud unicornio ninja")