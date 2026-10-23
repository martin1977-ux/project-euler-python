numero = 20
divisor = 1
flag = False

while flag == False:
    if numero % divisor == 0:
#        print (numero, "es divisible por", divisor)
        divisor +=1 
        if divisor == 21:
            flag = True
    else:
#        print (numero, "no es divisible por", divisor)
        numero +=20
        divisor = 1

print (numero)
