# -*- codin: utf-8 -*-

import sqlite3

conexao = sqlite3.connect("IMC.db")

cursor = conexao.cursor()
cursor.execute("SELECT * FROM  IMC")

resultado = cursor.fetchone()
print("Nome: %s\nAltura: %.2fm\nPeso: %.2fkg\nIMC: %.2f" %(resultado))


cursor.close()
conexao.close()