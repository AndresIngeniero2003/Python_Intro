#Menu
print("**********<Desafia de calificaciones y estadisticas>**********")
Inicio = True

while Inicio:
    opcion = int(input("""
        **********<Menu principal>**********

        1. Ingresar un calificacion(0 al 100)
        2. Ingresar varias calificaciones
        3. Salir
        Opcion -->  """))
    
    match opcion:
        case 1:
            print("")
            calificacion = int(input("Calificacion a ingresar:  "))
            if 0 <= calificacion <= 100:
                if calificacion>=80:
                    print("Felicitaciones pasastes con una calificacion muy alta estas aprobado!\n")
                elif calificacion>=60:
                    print("Felicidades has aprobado pero puedes seguir mejorando")
                elif calificacion>=55:
                    print("Has aprobado pero estas muy raspado no te descuides!")
                else:
                    print("Calificacion baja has reprobrado.\n")
            else:
                print("La calificacion ingresada esta fuera del rango intenta de nuevo\n")
        case 2:
            print("Debes ingresar las calificaciones separadas por comas")
            strCalificaciones = (input("Calificaciones a ingresar:  "))
            lista_str = strCalificaciones.split(',')
            lista_Cal = [int(cal.strip()) for cal in lista_str]
            print("Calificaciones agregadas -->  ", lista_Cal)
            Inicio2 = True
            while Inicio2:
                print("")
                opcion2 = int(input("""
            *************<Sub menu>*************

            1. Calcular promedio de las calificaciones ingresadas
            2. Ingresar un valor y mostrar cuantos son mayores a el
            3. Validar si una calificacion se encuentra en la lista y cuantas veces aparece
            4. Volver al menu principal
            Opcion -->  """))
            
                match opcion2:
                    case 1:                        
                        print("Calculando promedio..........\n")
                        suma = 0                
                        for elemento in lista_Cal:
                            suma = suma + elemento
                            promedio = suma/(len(lista_Cal))
                        print("El promedio de tu lista de calificaciones es: ",promedio)
                        print("")
                    case 2:
                        cal = int(input("Calificacion:  "))
                        Esta = False
                        for elemento in lista_Cal:
                            if elemento == cal:
                                Esta = True
                        if Esta:
                            longitud = len(lista_Cal)
                            indice = 0
                            contador = 0
                            while indice<longitud:
                                if cal < lista_Cal[indice]:
                                    contador += 1
                                indice += 1
                            print(f"Ingresaste la calificacion {cal} y en la lista {contador} son mayores que el")
                        else:
                            print("La calificacion ingresada no esta en la lista") 
                    case 3:
                        cal = int(input("Calificacion:  "))
                        print("Buscando calificacion...........")
                        cont = 0
                        for elemento in lista_Cal:
                            if cal != elemento:
                                continue

                            cont_local = 0
                            for ele in lista_Cal:
                                if cal == ele:
                                    cont_local += 1
                            cont = cont_local
                            break
                        if cont>0:
                            print(f"La calificacion {cal} se encuenta en la lista y aparece {cont} veces.")
                        else:
                            print(f"La calificacion {cal} no aparece en la lista")
                    case 4:
                        print("Regresando al menu principal...........")
                        Inicio2 = False
                    case _:
                        print("Opcion incorrecta!")
                        Inicio2 = False
        case 3:
            print("Cerrando programa......................") 
            Inicio = False
        case _:
            print("Opcion incorrecta!")
            Inicio = False

