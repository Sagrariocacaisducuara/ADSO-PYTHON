def juego(pregunta ):
    if pregunta == "si" or pregunta == "Si":
        print("Haz respondido mal, fin del juego")
    elif pregunta ==1:
        pregunta = int(input("¿La independencia de Colombia fue en el año 1810? (1. Si 2.No\n"))
        if pregunta != 1:
            print("Haz respondido mal, fin del juego")
        elif pregunta ==1:
            pregunta = int(input("The Doors fue un grupo de Rock Americano (1. Si 2.No\n"))
            if pregunta != 2:
                print("Haz respondido mal, fin del juego")
            else:
                print("Haz ganado el juego")

pregunta = input("¿Colón descubrió a America?")

juego(pregunta ) 