# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 18:46:12 2025

@author: nunol
"""

def main():
    print("Este programa calcula o valor futuro de um investimento")
    montante = eval(input("Introduza o montante inicial: "))
    juros = eval(input("Qual é o valor da taxa de juro: "))
    anos = eval(input("Qual a duração de investimento: "))
    for i in range (anos):
        montante = montante * (1 + (juros * .01))
        print("O valor daqui a", anos, "anos é", montante)
main()