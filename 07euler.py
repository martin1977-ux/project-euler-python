numero = 2
cantidad_primos = 0


while cantidad_primos < 10001:

    divisor = 2
    es_primo = True

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    
    if es_primo == True:
        cantidad_primos += 1
        print (cantidad_primos, "primos", numero, "es el numero")

    numero += 1

print ("El sexto numero primo es ", numero -1)
