def safenumber(listy):
    listo = listy.split(" ")
    for duck in listo:
        print(duck)
        numone = int(duck) + 1
        print(numone)
        listo.remove(duck)
        numtwo = int(duck[+1]) + 2
        print(numtwo)
        print("end")


safenumber("25 26 29 30 32 35 37 35")