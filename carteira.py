# -*- coding: utf-8 -*-
"""
Exercício aprendido em: https://youtu.be/47bf2ZLkvxgg

"""
#saldo declarado nas variaveis: saldo_daniel e saldo_joao
saldo_daniel = 200
saldo_joao = 230

logar = str(input("Nome de usuário: "))
if logar == "daniel":
    saldo_daniel_pagar = float(input("Valor a pagar: "))
    if saldo_daniel >= saldo_daniel_pagar:
        novo_saldo_daniel = (saldo_daniel - saldo_daniel_pagar)
    print("Seu saldo atual é R$: ", novo_saldo_daniel)

elif logar == "joao":
    saldo_joao_pagar = float(input("Valor a pagar: "))
    if saldo_joao >= saldo_joao_pagar:
            novo_saldo_joao = (saldo_joao - saldo_joao_pagar)
            print("Seu saldo atual é R$: ", novo_saldo_joao)
else:
    print("Saldo insuficiente!")
