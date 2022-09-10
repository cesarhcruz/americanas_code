"""
Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha uma média superior ou igual a 7 e "Reprovado", caso a média seja inferior a 7.
"""

nota1 = float(input("Qual é a nota do 1º Bimestre? "))
nota2 = float(input("Qual é a nota do 2º Bimestre? "))
nota3 = float(input("Qual é a nota do 3º Bimestre? "))
nota4 = float(input("Qual é a nota do 4º Bimestre? "))
presenca = float(input("Qual é a porcentagem de presença? "))

media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 7.0 and presenca >= 70:
    print("Você está aprovado(a)!, sua média foi ", media)
elif media >= 5.0 and presenca >= 70:
    print("Você está de Recuperação!, sua média foi ", media)
else:
    print("Você está reprovado(a)!, sua média foi ", media)
