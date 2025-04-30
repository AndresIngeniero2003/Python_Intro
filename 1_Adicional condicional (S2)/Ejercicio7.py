# 🔹 7️⃣ Detector de spam en correos electrónicos 📧

print("Detector de spam")
print()
mensaje = input("Ingresa cualquier mensaje que ha llegado a tu correo los últimos días -->  ").lower() 

palabras_spam = ["gratis", "gana dinero", "descuento exclusivo", "oferta especial", "haz clic aquí", "premio"]
es_spam = False 

for palabra in palabras_spam:
    if palabra in mensaje:
        es_spam = True
        break 

if es_spam:
    print("Este mensaje parece ser SPAM")
else:
    print("Este mensaje parece estar bien.")