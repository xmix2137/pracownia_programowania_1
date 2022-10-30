#Która_kwarta
x = int(input("Wprowadź współżędną x tego punktu: "))
y = int(input("Wprowadź współżędną y tego punktu: "))
if x>0 and y>0:
    print("Punkt znajduje się w 1 kwarcie")
elif x>0 and y<0:
    print("Punkt znajduje się w 2 kwarcie")
elif x<0 and y<0:
    print("Punkt znajduje się w 3 kwarcie")
elif x<0 and y>0:
    print("Punkt znajduje się w 4 kwarcie")
elif x==0 or y==0:
    print("Punkt znajduje się na osi układu współrzędnych")