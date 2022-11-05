#kalkulator sumy i średniej

suma = 0
srednia = 0
licznosc = 0
n = 1



while n != 0:
    n = int(input("Podaj liczbę: "))
    licznosc +=1
    suma = suma + n
    srednia = suma / licznosc
    print ("Podana liczba to: ", n)
    

print ("Liczność to: ", licznosc, "Suma to: ", suma, "Srednia to: ", srednia)

