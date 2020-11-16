limite = 100
numero = 1
contador = 1
numPrimos = 0
print('Números Primos de 1 a 100:')
while numero < limite:
    i = numero - 1
    while i > 1:
        if numero % i == 0: break
        i -= 1
        contador += 1
    else:
        print(numero)
        numPrimos += 1
    numero += 1

print('\nForam encontrados %d números primos.' %(numPrimos))
print('Fizemos %d comparações.' %(contador))