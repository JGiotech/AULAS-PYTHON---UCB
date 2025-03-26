#CRIANDO UM JOGO DE PAPEL E TESOURA

print("-------------------------------------------------------------------------------")
print("------------ BEM VINDO AO JOGO PEDRA PAPEL E TESOURA EM PYTHON ----------------")
print("-------------------------------------------------------------------------------")


# jogador1 = input("JOGADOR 1 DIGITE SUA ESCOLHA :  ")
# jogador2 = input("JOGADOR 2 DIGITE SUA ESCOLHA :  ")

# if jogador1 == jogador2:
#     print("Empate")

# elif (jogador1 == "papel" and jogador2 == "pedra") or \
#      (jogador1 == "pedra" and jogador2 == "tesoura") or \
#      (jogador1 == "tesoura" and jogador2 == "papel"):
#     print("Jogador 1 ganhou!")

# elif (jogador2 == "papel" and jogador1 == "pedra") or \
#      (jogador2 == "pedra" and jogador1 == "tesoura") or \
#      (jogador2 == "tesoura" and jogador1 == "papel"):
#     print("Jogador 2 ganhou!")

   
# else:
#     ("Você não digitou corretamente as opções aceitas, tente digitar 'pedra', 'papel', 'tesoura'")



while True:
    jogador1 = input("JOGADOR 1 DIGITE SUA ESCOLHA :  ")
    jogador2 = input("JOGADOR 2 DIGITE SUA ESCOLHA :  ")

    if jogador1 not in ["pedra", "papel", "tesoura"] or jogador2 not in ["pedra", "papel", "tesoura"]:
        print("Opção inválida!")
        continue

    if jogador1 == jogador2:
        print("Empate")

    elif (jogador1 == "papel" and jogador2 == "pedra") or \
      (jogador1 == "pedra" and jogador2 == "tesoura") or \
      (jogador1 == "tesoura" and jogador2 == "papel"):
        print("Jogador 1 ganhou!")

    elif (jogador2 == "papel" and jogador1 == "pedra") or \
     (jogador2 == "pedra" and jogador1 == "tesoura") or \
      (jogador2 == "tesoura" and jogador1 == "papel"):
     print("Jogador 2 ganhou!")

    jogar_novamente = input("Deseja jogar novamente? (s / n):  ")

    if jogar_novamente != ("s"):
        print("---------------")
        print("Até a proxima!")
        print("---------------")
        break
  
