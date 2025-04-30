#8. Validación de contraseña segura
contra = input("Ingresa una contraseña: ")

longitud = len(contra)

if longitud>=8:
    if "123" not in contra:
        print("Contraseña segura!")
    else:
        print("Contraseña insegura no puedes tener la seguencia <123>")
else:
    print("Contraseña insegura su longitud debe ser mayor a 7")

