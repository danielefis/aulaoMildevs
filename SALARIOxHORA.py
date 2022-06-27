# -*- coding: utf-8 -*-
"""
Exercício aprendido em: https://youtu.be/47bf2ZLkvxgg

"""
salario = float(input("Valor do seu salário? "))
hora = float(input("Horas trabalhada por dia? "))
horaX = hora * 30
horaTrabalhada = salario / horaX
print(f"Valor por hora R$: {horaTrabalhada:.2f}")
