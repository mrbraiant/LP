# -*- codin: utf-8 -*-

import sqlite3

nome = str(input("Digite seu nome: "))
altura = float(input('Digite sua Altura substituindo a VIRGULA por PONTO: '))
peso = float(input('Digite seu Peso: '))
altX2 = (altura*altura)
imc = (peso/altX2)

conexao = sqlite3.connect("IMC.db")

cursor = conexao.cursor()
cursor.execute("CREATE TABLE IMC(nome varchar(20), altura float, peso float, imc float)")

cursor.execute("INSERT INTO IMC(nome, altura, peso, imc) VALUES(?,?,?,?)",(nome, altura, peso, imc))

conexao.commit()

cursor.close()
conexao.close()