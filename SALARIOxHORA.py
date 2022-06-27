# -*- coding: utf-8 -*-
"""
Exercício aprendido em: https://youtu.be/47bf2ZLkvxgg

"""
salario = float(input("Valor do seu salário? "))
hora = float(input("Horas trabalhada por dia? "))
dias = int(input("Dias trabalhado no mês? "))
horaX = hora * dias
horaTrabalhada = salario / horaX
print(f"Valor por hora R$: {horaTrabalhada:.2f} O seu salário total em {dias} dias é de R$ {salario:.2f}")
