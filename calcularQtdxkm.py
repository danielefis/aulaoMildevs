# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 18:33:48 2022

@author: danielefis
"""

qtdH = int(input("Informe a quantidade de horas: "))
vlcd = float(input("Qual foi a velocidade média: "))

distancia = qtdH * vlcd

litros = distancia / 12 
print("Distância: ",distancia)
print("Litros: ",litros)