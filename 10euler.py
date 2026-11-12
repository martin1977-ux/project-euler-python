numero = 3
suma = 2


while numero < 2000000:

    divisor = 2
    es_primo = True

    while  divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    
    if es_primo:
        suma += numero

    numero += 1

print ("La suma total es: ", suma )
