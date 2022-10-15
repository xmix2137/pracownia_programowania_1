#wzor herona
import math

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

if a<(b+c) and b<(a+c) and c<(a+b):
    p =float((a+b+c)/2)
    S = math.sqrt((p*(p-a)*(p-b)*(p-c)))
    print("Pole trojkata wynosi: ", S)
else: 
    print("Nie jest to trojkat")