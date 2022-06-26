# -*- coding: utf-8 -*-
"""
Exercício aprendido em: https://youtu.be/47bf2ZLkvxgg

"""

salario = float(input("Informe o salário: "))
aumento = salario * 0.15
novoSalario = aumento+salario
inss = novoSalario * 0.11
fgts = novoSalario * 0.08
multa = float(input("Digite o  valor da multa: "))
desconto = inss + fgts + multa
salarioFinal = novoSalario-desconto
print("Salário inicial:", salario)
print("Salário reajustado:", novoSalario)
print(f"O desconto do INSS é {fgts} e INSS {inss}")
print("Valor da multa:", multa)
print("Total de descontos INSS+FGTS+MULTA",desconto)
print("Salário final R$", salarioFinal)
