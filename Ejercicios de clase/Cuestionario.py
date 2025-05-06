#Preguntas con puntaje red flas
print("Inicio de preguntas")
print("")
print("*******************************************************")
puntaje = 0
pregunta1 = input("¿Estudias? ")
if pregunta1.lower() == "si" or pregunta1.lower() == "no":
    if pregunta1  == "si":
        puntaje = puntaje + 100
        pregunta2 = input("¿Trabajas? ")
        if pregunta2.lower() == "si":
            puntaje = puntaje + 100
            pregunta3 = input("¿Cual es tu tono de piel?(blanca - morena - negra) ")
            if pregunta3.lower() == "blanca":
                puntaje = puntaje + 100
                pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                if pregunta4.lower() == "rubio":
                    puntaje = puntaje + 100
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
                elif pregunta4.lower() == "negro":
                    puntaje = puntaje + 80
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
                elif pregunta4.lower() == "rojo":
                    puntaje = puntaje + 80
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
            elif pregunta3.lower() == "morena":
                puntaje = puntaje + 50
                pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                if pregunta4.lower() == "rubio":
                    puntaje = puntaje + 0
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
                elif pregunta4.lower() == "negro":
                    puntaje = puntaje + 100
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
                elif pregunta4.lower() == "rojo":
                    puntaje = puntaje + 0
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
            elif pregunta3.lower() == "negra":
                puntaje = puntaje + 0
                pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                if pregunta4.lower() == "rubio":
                    puntaje = puntaje + 0
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
                elif pregunta4.lower() == "negro":
                    puntaje = puntaje + 50
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
                elif pregunta4.lower() == "rojo":
                    puntaje = puntaje + 0
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
            else:
                print("opcion incorrecta 0 puntos")
                pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                if pregunta4.lower() == "rubio":
                    puntaje = puntaje + 100
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
                elif pregunta4.lower() == "negro":
                    puntaje = puntaje + 80
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
                elif pregunta4.lower() == "rojo":
                    puntaje = puntaje + 80
                    pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                    if pregunta5.lower() == "no salgo":
                        puntaje = puntaje + 60
                    elif pregunta5.lower() == "poco":
                        puntaje = puntaje + 100
                    elif pregunta5.lower() == "seguido":
                        puntaje = puntaje + 80
                    elif pregunta5.lower() == "mucho":
                        puntaje = puntaje + 0
                    else:
                        print("Opcion incorrecta")
        else:
            puntaje = puntaje + 0
            pregunta2 = input("¿Trabajas ")
            if pregunta2.lower() == "si":
                puntaje += 100
                pregunta3 = input("¿Cual es tu tono de piel?(blanca - morena - negra) ")
                if pregunta3.lower() == "blanca":
                    puntaje = puntaje + 100
                    pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                    if pregunta4.lower() == "rubio":
                        puntaje = puntaje + 100
                        pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                        if pregunta5.lower() == "no salgo":
                            puntaje = puntaje + 60
                        elif pregunta5.lower() == "poco":
                            puntaje = puntaje + 100
                        elif pregunta5.lower() == "seguido":
                            puntaje = puntaje + 80
                        elif pregunta5.lower() == "mucho":
                            puntaje = puntaje + 0
                        else:
                            print("Opcion incorrecta")
                    elif pregunta4.lower() == "negro":
                        puntaje = puntaje + 80
                        pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                        if pregunta5.lower() == "no salgo":
                            puntaje = puntaje + 60
                        elif pregunta5.lower() == "poco":
                            puntaje = puntaje + 100
                        elif pregunta5.lower() == "seguido":
                            puntaje = puntaje + 80
                        elif pregunta5.lower() == "mucho":
                            puntaje = puntaje + 0
                        else:
                            print("Opcion incorrecta")
                    elif pregunta4.lower() == "rojo":
                        puntaje = puntaje + 80
                        pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                        if pregunta5.lower() == "no salgo":
                            puntaje = puntaje + 60
                        elif pregunta5.lower() == "poco":
                            puntaje = puntaje + 100
                        elif pregunta5.lower() == "seguido":
                            puntaje = puntaje + 80
                        elif pregunta5.lower() == "mucho":
                            puntaje = puntaje + 0
                        else:
                            print("Opcion incorrecta")
                elif pregunta3.lower() == "morena":
                    puntaje = puntaje + 50                    
                    pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                    if pregunta4.lower() == "rubio":
                        puntaje = puntaje + 0
                        pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                        if pregunta5.lower() == "no salgo":
                            puntaje = puntaje + 60
                        elif pregunta5.lower() == "poco":
                            puntaje = puntaje + 100
                        elif pregunta5.lower() == "seguido":
                            puntaje = puntaje + 80
                        elif pregunta5.lower() == "mucho":
                            puntaje = puntaje + 0
                        else:
                            print("Opcion incorrecta")
                    elif pregunta4.lower() == "negro":
                        puntaje = puntaje + 100
                        pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                        if pregunta5.lower() == "no salgo":
                            puntaje = puntaje + 60
                        elif pregunta5.lower() == "poco":
                            puntaje = puntaje + 100
                        elif pregunta5.lower() == "seguido":
                            puntaje = puntaje + 80
                        elif pregunta5.lower() == "mucho":
                            puntaje = puntaje + 0
                        else:
                            print("Opcion incorrecta")
                    elif pregunta4.lower() == "rojo":
                        puntaje = puntaje + 0
                        pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                        if pregunta5.lower() == "no salgo":
                            puntaje = puntaje + 60
                        elif pregunta5.lower() == "poco":
                            puntaje = puntaje + 100
                        elif pregunta5.lower() == "seguido":
                            puntaje = puntaje + 80
                        elif pregunta5.lower() == "mucho":
                            puntaje = puntaje + 0
                        else:
                            print("Opcion incorrecta")
                elif pregunta3.lower() == "negra":
                    puntaje = puntaje + 0
                    pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                    if pregunta4.lower() == "rubio":
                        puntaje = puntaje + 0
                        pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                        if pregunta5.lower() == "no salgo":
                            puntaje = puntaje + 60
                        elif pregunta5.lower() == "poco":
                            puntaje = puntaje + 100
                        elif pregunta5.lower() == "seguido":
                            puntaje = puntaje + 80
                        elif pregunta5.lower() == "mucho":
                            puntaje = puntaje + 0
                        else:
                            print("Opcion incorrecta")
                    elif pregunta4.lower() == "negro":
                        puntaje = puntaje + 50
                        pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                        if pregunta5.lower() == "no salgo":
                            puntaje = puntaje + 60
                        elif pregunta5.lower() == "poco":
                            puntaje = puntaje + 100
                        elif pregunta5.lower() == "seguido":
                            puntaje = puntaje + 80
                        elif pregunta5.lower() == "mucho":
                            puntaje = puntaje + 0
                        else:
                            print("Opcion incorrecta")
                    elif pregunta4.lower() == "rojo":
                        puntaje = puntaje + 0
                        pregunta5 = input("¿Que tando sales de fiesta? (no salgo - poco - seguido - mucho) ")
                        if pregunta5.lower() == "no salgo":
                            puntaje = puntaje + 60
                        elif pregunta5.lower() == "poco":
                            puntaje = puntaje + 100
                        elif pregunta5.lower() == "seguido":
                            puntaje = puntaje + 80
                        elif pregunta5.lower() == "mucho":
                            puntaje = puntaje + 0
                        else:
                            print("Opcion incorrecta")
                else:
                    print("opcion incorrecta 0 puntos")
    else:
        puntaje = puntaje + 0
        pregunta2 = input("¿Trabajas ")
        if pregunta2.lower() == "si":
            puntaje = puntaje + 100
            pregunta3 = input("¿Cual es tu tono de piel?(blanca - morena - negra) ")
            if pregunta3.lower() == "blanca":
                puntaje = puntaje + 100
                pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                if pregunta4.lower() == "rubio":
                    puntaje = puntaje + 100
                elif pregunta4.lower() == "negro":
                    puntaje = puntaje + 80
                elif pregunta4.lower() == "rojo":
                    puntaje = puntaje + 80
            elif pregunta3.lower() == "morena":
                puntaje = puntaje + 50
                pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                if pregunta4.lower() == "rubio":
                    puntaje = puntaje + 0
                elif pregunta4.lower() == "negro":
                    puntaje = puntaje + 100
                elif pregunta4.lower() == "rojo":
                    puntaje = puntaje + 0
            elif pregunta3.lower() == "negra":
                puntaje = puntaje + 0
                pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                if pregunta4.lower() == "rubio":
                    puntaje = puntaje + 0
                elif pregunta4.lower() == "negro":
                    puntaje = puntaje + 50
                elif pregunta4.lower() == "rojo":
                    puntaje = puntaje + 0
            else:
                print("opcion incorrecta, 0 puntos")
        else:
            puntaje = puntaje + 0  
            pregunta3 = input("¿Cual es tu tono de piel?(blanca - morena - negra) ")
            if pregunta3.lower() == "blanca":
                puntaje = puntaje + 100
                pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                if pregunta4.lower() == "rubio":
                    puntaje = puntaje + 100
                elif pregunta4.lower() == "negro":
                    puntaje = puntaje + 80
                elif pregunta4.lower() == "rojo":
                    puntaje = puntaje + 80
            elif pregunta3.lower() == "morena":
                puntaje = puntaje + 50
                pregunta4 = input("¿De qué color es tu cabello? (rubio - negro - rojo) ")
                if pregunta4.lower() == "rubio":
                    puntaje = puntaje + 0
                elif pregunta4.lower() == "negro":
                    puntaje = puntaje + 100
                elif pregunta4.lower() == "rojo":
                    puntaje = puntaje + 0
            elif pregunta3.lower == "negra":
                puntaje = puntaje + 0
                pregunta4 = input("¿De que color es tu cabello?(rubio - negro - rojo) ")
                if pregunta4.lower() == "rubio":
                    puntaje = puntaje + 0
                elif pregunta4.lower() == "negro":
                    puntaje = puntaje + 50
                elif pregunta4.lower() == "rojo":
                    puntaje = puntaje + 0
            else:
                print("opcion incorrecta 0 puntos")
else:
    print("Opción incorrecta!")

    
print(puntaje)
