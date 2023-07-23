import random as rd

def jogoPapelPedraTesoura():

  vitoria1 = 0
  vitoria2 = 0
  rodada = 0

  player1 = str(input('Digite o nome do jogador número 1: '))
  player2 = str(input('Digite o nome do jogador número 2: '))



  while vitoria1 <= 2 and vitoria2 <= 2:
    primeiraJogada = rd.choice(["papel", "pedra", "tesoura"])
    segundaJogada = rd.choice(["papel", "pedra", "tesoura"])
    rodada+=1

    if primeiraJogada == 'papel' and segundaJogada == 'pedra':
      vitoria1+=1
      print(f'{player1} ganhou a rodada, papel vence pedra')

    if primeiraJogada == 'pedra' and segundaJogada == 'tesoura':
      vitoria1+=1
      print(f'{player1} ganhou a rodada, pedra vence tesoura')

    if primeiraJogada == 'tesoura' and segundaJogada == 'papel':
      vitoria1+=1
      print(f'{player1} ganhou a rodada, tesoura vence papel')

    if primeiraJogada == 'pedra' and segundaJogada == 'papel':
      vitoria2+=1
      print(f'{player2} ganhou a rodada, papel vence pedra')

    if primeiraJogada == 'tesoura' and segundaJogada == 'pedra':
      vitoria2+=1
      print(f'{player2} ganhou a rodada, pedra vence tesoura')

    if primeiraJogada == 'papel' and segundaJogada == 'tesoura':
      vitoria2+=1
      print(f'{player2} ganhou a rodada, tesoura vence papel')

    if primeiraJogada == segundaJogada:
      print("empate, joguem novamente")

  if vitoria1 > vitoria2:
      print(f'{player1}  \033[32m' 'ganhou com',f'{vitoria1}'' vitórias! ')
      print('após', f'{rodada} rodadas jogadas')

  else:
      print(f'{player2}  \033[32m''ganhou!',f'{vitoria2}'' vitórias! ')
      print('após', f'{rodada} rodadas jogadas')


jogoPapelPedraTesoura()
















