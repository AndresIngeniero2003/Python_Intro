# 🔹 2️⃣ Asistente de productividad ⏳

print("Bievenido soy tu asistente Andrea Dominguez!")
print("")
dia = input("Ingresa el dia de hoy: (lunes, martes, miercoles, jueves, viernes, sabado,domingo)    -->   ")
print("")
print("Formato militar 24 horas")
hora = int(input("Ingresa la hora: "))
min = int(input("Ingresa los minutos: "))
print("")
print("La hora actual es -->" , hora, ":" , min)
print("")

match dia.lower() :
    case "lunes":
        if hora < 14 or hora > 6:
            print("Andrea: Horario de trabajo ten la mejor disposicion!")
        elif hora < 17 or hora > 14:
            print("Andrea: Puedes entrenarte te envio mucha energia!")
        elif hora > 17:
            print("Andrea: Horario de descanso tomate tu tiempo para recuper energias")
        else:
            print("Hora ingresa incorrecta revisa tu respuesta.....")
    case "martes":
        if hora < 14 or hora > 6:
            print("Andrea: Horario de trabajo ten la mejor disposicion!")
        elif hora < 17 or hora > 14:
            print("Andrea: Puedes entrenarte te envio mucha energia!")
        elif hora > 17:
            print("Andrea: Horario de descanso tomate tu tiempo para recuper energias")
        else:
            print("Hora ingresa incorrecta revisa tu respuesta.....")
    case "miercoles":
        if hora < 14 or hora > 6:
            print("Andrea: Horario de trabajo ten la mejor disposicion!")
        elif hora < 17 or hora > 14:
            print("Andrea: Puedes entrenarte te envio mucha energia!")
        elif hora > 17:
            print("Andrea: Horario de descanso tomate tu tiempo para recuper energias")
        else:
            print("Hora ingresa incorrecta revisa tu respuesta.....")
    case "jueves":
        if hora < 14 or hora > 6:
            print("Andrea: Horario de trabajo ten la mejor disposicion!")
        elif hora < 17 or hora > 14:
            print("Andrea: Puedes entrenarte te envio mucha energia!")
        elif hora > 17:
            print("Andrea: Horario de descanso tomate tu tiempo para recuper energias")
        else:
            print("Hora ingresa incorrecta revisa tu respuesta.....")
    case "viernes":
        if hora < 14 or hora > 6:
            print("Andrea: Horario de trabajo ten la mejor disposicion!")
        elif hora < 17 or hora > 14:
            print("Andrea: Puedes entrenarte te envio mucha energia!")
        elif hora > 17:
            print("Andrea: Horario de descanso tomate tu tiempo para recuper energias")
        else:
            print("Hora ingresa incorrecta revisa tu respuesta.....")
    case "sabado":
        print("Andrea: Dias de descanso utilizalos para hacer cualquier actividad que te guste")
    case "domingo":
        print("Andrea: Dias de descanso utilizalos para hacer cualquier actividad que te guste")
    case _:
        print("")
        print("Dia incorrecto revisa tu respuesta...")
        print(dia)
    
    