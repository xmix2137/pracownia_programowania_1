#Obliczanie podatku VAT

a = float(input("Podaj kwotę od której chcesz obliczyć VAT: "))
b = round(a*0.23, 2)
print("Kwota to : ", a, "zŁ")
print("Naliczony podatek VAT od tej kwoty to: ", b, "zł")
