# -*- coding: utf-8 -*-

from random import randint
aleatorio = (randint(0,10))
fechar = ""
while fechar != 'fechar':
    numero = int(input("Digite um número: "))
    if numero == 11:
        fechar = str(input("Deseja fechar? Escreva: fechar"))
    elif aleatorio == numero:
        print("Você acertou!")
    elif aleatorio > numero:
        print("É maior!")
    else:
        print("É menor!")
