# 🔹 3️⃣ Control de acceso con doble autenticación 🔐

print("Control de acceso! super seguro de la NASA")
print("Cod = 123456")

print("")
print("..........<Creando usuario>..........")
print("")
us = input("Ingresa tu usuario -->  ")
con = input("Ingresa tu contraseña -->  ")
print("")
print("............<Encrytando>............")
print("")

print("..........<Iniciar sesion>..........")
print("")
us2 = input("Ingresa tu usuario -->  ")
con2 = input("Ingresa tu contraseña -->  ")
print("")
print("............<Validando>............")
print("")

if us == us2:
    print("Usuario correcto")
    if con == con2:
        print("Contraseña correcta")
        print("Enviando codigo de verificacion.......")
        cod = input("Ingresa codigo -->  ")
        print("")
        if cod == "123456":
            print("Acceso consedido")
        else:
            print("Acceso denegado")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto")



