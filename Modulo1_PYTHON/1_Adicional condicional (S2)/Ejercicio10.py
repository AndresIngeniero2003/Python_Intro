# 🔹 🔟 Evaluador de contraseñas seguras 🔑
# Diseña un programa que verifique si una contraseña es segura.
# Debe cumplir con:

#     Al menos 8 caracteres
#     Incluir números y letras
#     No contener espacios
#     🛡️ Dale retroalimentación al usuario sobre cómo mejorar su contraseña.
print("Validador de contraseñas seguras")
print("")
contraseña = input("Ingresa tu contraseña -->  ")
longitud = len(contraseña)
if longitud>=8:
    print("Longitud correcta")
    print("")
    
else:
    print("Longitud invalida, intentar con mas caracteres")