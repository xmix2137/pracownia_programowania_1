#piramida_gwiazdek
n = 10
for i in range(0,n):
    if i<=5:
        for j in range(0,i+1):
            print("*", end="")
        print("\r")
    else:
        for j in range(0,5):
            print("*", end="")
        print("\r")


