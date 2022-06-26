# -*- coding: utf-8 -*-
"""
Exercício aprendido em: https://youtu.be/47bf2ZLkvxgg mesttra

"""

salario = float(input("Informe o salário: "))
if salario <= 2000: #SE O SALARIO FOR IGUAL OU MENOR QUE 2000 REAJUSTE DE 15%
    aumento = salario * 0.15
else:
    aumento = salario * 0.05
novoSalario = aumento+salario
inss = novoSalario * 0.11
fgts = novoSalario * 0.08

desconto = inss + fgts
salarioFinal = novoSalario-desconto
print("Salário inicial:", salario)
print("Salário reajustado:", novoSalario)
print(f"O desconto do INSS é {inss:.2f} e INSS {fgts:.2f}")
print(f"Total de descontos de INSS+FGTS R$: {desconto:.2f}")
print(f"Salário final R$: {salarioFinal:.2f}")
