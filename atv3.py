# -*- codin:latin1 -*-

print('Programa para análise do número menor digitado\n...\n...')

a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número:'))

if a < b and a < c:
    print('O menor número é: %d'%(a))
if b < a and b < c:
    print('O menor número é: %d'%(b))
if c < a and c < b:
    print('O menor número é: %d'%(c))