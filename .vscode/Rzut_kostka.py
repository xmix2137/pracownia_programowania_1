#generator trzech rzutów kostką

import random

a = int(random.randrange(1,6,1))
print("Pierwszy rzut wynosi: ", a)
b = int(random.randrange(1,6,1))
print("Drugi rzut wynosi: ", b)
c = int(random.randrange(1,6,1))
print("Trzeci rzut wynosi: ", c)

d = a+b+c

print("Suma tych trzech rzutów to: ", d)