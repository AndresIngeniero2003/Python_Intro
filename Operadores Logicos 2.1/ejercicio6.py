#6. Requisitos para obtener una beca
promedio = float(input("Ingresa tu promedio: "))
ingresos = float(input("Cuales son tus ingresos mensuales: "))
cantidad_m = int(input("Cantidad de materias: "))

beca = (promedio>=8) and (cantidad_m<3) and (ingresos<=1500)

if beca:
    print("Aplicas para la beca!")
else:
    print("No aplicas")


