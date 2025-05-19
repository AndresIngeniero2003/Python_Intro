#10. Horario permitido para clases
hora = int(input("Ingresa la hora(0-23): "))

if (hora>=0 and hora<=23):
    if (hora>=8 and hora<=18 and hora != 13):
        print("Horario permitido")
    else:
        print("Horario NO permitido")
else:
    print("Horario NO permitido")


