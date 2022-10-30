#karta_kredytowa
i = 0
p = str("0805")
for i in range (0,3):
    a = str(input("Podaj pin do karty: "))
    if a == p:
        print("Oto dostęp do twojego konta: ")
        break
    elif i == 2:
        print("Twoje konto zostało zablokowane")
    else:
        print("Spróbuj ponownie")
