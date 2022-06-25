# -*- coding: utf-8 -*-
"""
exercício de: https://youtu.be/47bf2ZLkvxg

"""

qtdH = int(input("Informe a quantidade de horas: "))
vlcd = float(input("Qual foi a velocidade média: "))

distancia = qtdH * vlcd

litros = distancia / 12 
print("Distância: ",distancia)
print("Litros: ",litros)
