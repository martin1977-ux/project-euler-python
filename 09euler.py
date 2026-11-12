a = 1
b = 2
c = 0
res = 0
encontrado = False

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2 and c > b:
            res = a * b * c
            print ("A = ", a,"B = ", b, "C = ", c)
            print ("El producto es: ", res)
            encontrado = True
            break
    if encontrado:
         break    


