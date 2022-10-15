#program ze zgadywaniem liczby oczek 

import random

a = int(random.randrange(1,6,1))

b = int(input("Zgaduj jaka to liczba, i mi ją podaj: "))

if b == a:
    print("Brawo udało ci się zgadnąć")
else:
    print("Niestety nie udało się, liczba to to:", a)

