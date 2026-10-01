a = 1
b = 2
c = 0
suma = b

while c < 4000000:
    c = a + b
    if c % 2 == 0 and c < 4000000:
        suma += c 
    a = b
    b = c

print (suma)
