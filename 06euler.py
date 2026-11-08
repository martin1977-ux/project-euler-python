suma = 0
suma_cuad = 0

for num in range (1, 101):
    suma = suma + num

suma = suma ** 2

print (suma)

for nume in range (1, 101):
    suma_cuad = suma_cuad + nume ** 2

print (suma_cuad)

print ("La diferencia es: ", suma - suma_cuad)
