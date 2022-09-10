# > WHILE > ESTRUTURA DE REPETIÇÃO

numero_sorteado = 15

numero_escolhido = int(input("Informe um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print("Você erro! Tente novamente: ")

    numero_escolhido = int(input("Informe um número entre 1 e 20: "))

print("Você acertou")