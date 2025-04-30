# 🔹 1️⃣ Sistema de recomendaciones de películas 🎬

print("Sistema de recomendacion de peliculas!")
print(" ")
edad = int(input("Ingresa tu edad por favor: "))
preferencia = input("Que prefieres ver: accion, comedia, terror, anime    -->  ")
print("")

match preferencia.lower():
    case "accion":
        if edad > 13:
            print("Te recomendare peliculas para mayores")
            print("")
            print("Shang Chi y la leyenda de los diez anillos")
            print("El último gran héroe")
            print("El sexto día")
        else:
            print("Te recomendare peliculas para menores")
            print("")
            print("Tortugas Ninja: Caos Mutante")
            print("Toy Story")
            print("Paddington: Aventura en la selva")
    case "comedia":
        if edad > 13:
            print("Te recomendare peliculas para mayores")
            print("")
            print("Shang Chi y la leyenda de los diez anillos")
            print("El último gran héroe")
            print("El sexto día")
        else:
            print("""Para menores de 13 años, las comedias suelen ser animadas o con un enfoque familiar, 
                  centradas en temas como la amistad, la escuela, y la vida cotidianas""")
            print("")
            print("Intensamente")
            print("Encanto")
            print("MI vecino totoro")
    case "terror":
        if edad > 13:
            print("Te recomendare peliculas para mayores")
            print("")
            print("Asesinos en serie")
            print("Annabelle")
            print("La casa del terror")
        else:
            print("No hay peliculas de terror para menores")
    case "anime":
        print("Disfruta de los mejores animes")
        print("")
        print("Naruto")
        print("Dragon ball z")
        print("Los caballeros del zodiaco")
    case _:
        print("Opcion invalida")

