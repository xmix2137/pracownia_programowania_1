#psi_wiek
a = float(input("Wprowadź wiek swojego psa: "))
if a == 1:
    print("Twój pies ma 10,5 psich lat")
elif a ==2:
    print("Twój pies ma 21 psich lat")
elif a>2:
    b = float((a-2)*4+21)
    print("Twój pies ma", b, "lat" )