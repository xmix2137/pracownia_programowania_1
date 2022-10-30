#Liczba_w_najmniejszych_monetach
a = int(input("Podaj dostępną kwotę: "))
x = 0
y = 0
z = 0
while a%5 == 0:
    x+=1
    a = a-5
while a%2 == 0:
    y+=1
    a = a-2
while a%1 ==0:
    z+=1
    z = z-1
print("Będzie to ",x, "monet 5zł", y,"monet 2zł", "i", z, "monet 1zł")
