#3. Verificación para participar en un concurso internacional
pais = input("ingresa tu pais: ")
edad = int(input("ingresa tu edad: "))
documento = int(input("ingresa tu numero de documento: "))

if (edad>=18 and edad<=30) and (pais != "Antártida") and (documento != 0):
    print("Cumples las condiciones")
else:
    print("No cumples")

