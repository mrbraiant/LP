# *-* codin:latin1 *-*

'''
textoInvertido = input('Digite o Texto para inverter a ordem das letras:')
string = textoInvertido[::-1]
print('O Texto digitado é %s \ne o texto invertido: %s'%(textoInvertido,string))
'''
frase = input('Digite uma Frase para ser invertida:')
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('A frase digitada foi: {}\ne a frase invertida é: {}'.format(frase,invertida))
