# 🔹 5️⃣ Asistente de clima y vestimenta 🌦️
print("Asistente de clima y vestimenta")
print("")
tem = float(input("Ingresa la temperatura -->  "))
lluvia = input("Esta lloviendo? (si/no) -->  ")

if lluvia.lower() == "si":
    if tem < 25 :
        print("Te recomiendo llevar un abrigo y un paragua para la lluvia")
    else:
        print("Abrigate bien puedes estar tranquilo pronto dejara de llover")
else:
    if tem < 25 :
        print("Puedes llevar ropa lijera y tal vez un paragua por si de pronto llueve")
    else:
        print("Puedes llevar ropa lijera no hay problemas de lluvia")
    
