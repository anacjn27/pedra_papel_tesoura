opcoes = ["Pedra", "Papel", "Tesoura"]
contador = 0
vitorias_jogador1 = 0
vitorias_jogador2 = 0

while contador < 5:
    print('Jogo Pedra, Papel ou Tesoura entre dois jogadores!')

    jogador1= input("Jogador 1 escolha: Pedra, Papel ou Tesoura? ")
    jogador2= input("Jogador 2 escolha: Pedra, Papel ou Tesoura? ")

    if jogador1 not in opcoes or jogador2 not in opcoes:
        print("Opção inválida de um dos jogadores. Tentem novamente")
        continue

    if jogador1 == jogador2:
        print("Empate")

    elif jogador1 == "Pedra" and jogador2 == "Tesoura":
        print("Jogador 1 Venceu!")

    elif jogador1 == "Papel" and jogador2 == "Pedra":
        print("Jogador 1 Venceu!")

    elif jogador1 == "Tesoura" and jogador2 == "Papel":
        print("Jogador 1 Venceu!")
        vitorias_jogador1 += 1
    else:
        print("Jogador 2 Venceu!")
        vitorias_jogador2 += 1


    contador += 1

    print("Resultado final: ")

    if vitorias_jogador1 > vitorias_jogador2:
        print(f"Jogador 1 venceu com {vitorias_jogador1} vitórias!")

    elif vitorias_jogador2 > vitorias_jogador1:
        print(f"Jogador 2 venceu com {vitorias_jogador2} vitórias!")

    else:
        print("O jogo terminou em empate!")

    