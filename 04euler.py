mayor = 0

for a in range(100, 1000):
    for b in range(100, 1000):
        resultado = a * b
        numero = str(resultado)
        num1 = numero[::-1]

        if numero == num1:
            if resultado > mayor:
                mayor = resultado

print ("El numero ", mayor, "es palindromo")


