numero = 600851475143

divisor = 2
es_primo = True
mayor_factor = 0

while divisor * divisor <= numero:
    if numero % divisor == 0:
        mayor_factor = divisor
        numero = numero // divisor
    else:
        divisor += 1

if numero > 1:
    mayor_factor = numero


print ("El mayor factor primo es ", mayor_factor)


