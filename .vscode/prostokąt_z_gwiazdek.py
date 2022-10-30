#prostokąt_z_gwiazdek

a = int(input("Podaj bok a prostokąta: "))
b = int(input("Podaj bok b prostokąta: "))

for i in range (1, a + 1):
	for j in range (1, b + 1):
		if i == 1 or i == a or j == 1 or j == b:
			print (end="*")
		else:
			print(end=" ")

	print (end="\n")