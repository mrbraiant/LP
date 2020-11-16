# -*- codin: latin1 -*-

DiasDVida = int(input('Digite sua idade considerando seus dias de vida:'))
ano = DiasDVida/365
meses = (DiasDVida % 365)/30
dia = (DiasDVida%365)%30

print('Você tem %d anos, %d meses e %d dias'%(ano,meses,dia))
