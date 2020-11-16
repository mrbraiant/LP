import math

a = int(input('Digite o lado A:'))
b = int(input('Digite o lado B:'))
c = int(input('Digite o lado C:'))

if a < b + c and b < a + c and c < a + b:
    print('A condição de existência de Trianulo é Válido para estas medidas! \o/\o/')
    #considerado como um triânulo equilátero
    h = (a*math.sqrt(3)/2)
    print('Area desse triângulo é: %.2f'%(h))
else:
    print('Triângulo inválido! =/ As medidas %d, %d e %d não permitem um Triângulo válido! :/'%(a,b,c))