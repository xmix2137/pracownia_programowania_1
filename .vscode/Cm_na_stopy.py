#Program przeliczający wzrost w cm na stopy
a = float(input("Podaj swój wzrost w centymetrach: "))
b = int (a/30.48)               #biore czesc calkowita z a/30.48 obliczajac stopy
c = (a/30.48-b)*12              #obliczam cale
print("W przeliczeniu na stopy mierzysz: ", b, "stop, oraz ", c ,"cali")