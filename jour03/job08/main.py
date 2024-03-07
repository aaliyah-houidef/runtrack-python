def food(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison =="été":
        print("Poire, fraise, cassis")
    elif type =="légumes" and saison =="hiver":
        print("carotte, topinambour, endive")
    elif type =="légumes" and saison =="été":
        print("artichaut, aubergine,navet")

food("fruits","été")