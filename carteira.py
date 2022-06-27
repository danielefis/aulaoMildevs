# -*- coding: utf-8 -*-
"""
Exercício aprendido em: https://youtu.be/47bf2ZLkvxgg

"""

saldo = 200
pagar = float(input("Valor a pagar: "))
if saldo >= pagar:
    novo_saldo = (saldo - pagar)
    print("Seu saldo atual é: ", novo_saldo)
