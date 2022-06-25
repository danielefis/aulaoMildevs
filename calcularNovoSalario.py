# -*- coding: utf-8 -*-
"""
Exercício aprendido em: https://youtu.be/47bf2ZLkvxgg

"""

salario = float(input("Informe o salário: "))
aumento = salario * 0.15
novoSalario = aumento+salario
inss = novoSalario * 0.11
fgts = novoSalario * 0.08
desconto = inss + fgts
salarioFinal = novoSalario-desconto
print("Salário inicial:", salario)
print("Salário reajustado:", novoSalario)
print("Desconto 11% INS R$:", inss)
print("Desconto 8% FGTS R$:", fgts)
print("Total de descontos INSS+FGTS R$", desconto)
print("Salário final R$", salarioFinal)
