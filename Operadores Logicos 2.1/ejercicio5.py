#5. Conexión segura en la red
protocolo = input("Escoge el protoclo de tu pagina(1.http 2.httos): ")
puerto = input("Escoge tu puerto(1. 80 2.443): ")

if protocolo.lower() == "2" and puerto == "2":
    print("Conexcion segura")
else:
    print("Conexcion insegura")

