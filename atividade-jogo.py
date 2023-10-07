print('Digite [1] para PEDRA \nDigite [2] para PAPEL \nDigite [3] para TESOURA')
jogador1 = int(input('JOGADOR 1: '))
jogador2 = int(input('JOGADOR 2: '))

if jogador1 != (1, 2, 3) and jogador2 != (1, 2, 3):
    print('Opção inválida')

while jogador1 == jogador2:
    print('Ninguém ganhou! Vamos jogar novamente!')
    jogador1 = int(input('JOGADOR 1: '))
    jogador2 = int(input('JOGADOR 2: '))

if jogador1 == 1 and jogador2 == 2:
    print('JOGADOR 2 VENCEU')
elif jogador1 == 1 and jogador2 == 3:
    print('JOGADOR 1 VENCEU')
elif jogador1 == 2 and jogador2 == 1:
    print('JOGADOR 1 VENCEU')
elif jogador1 == 2 and jogador2 == 3:
    print('JOGADOR 2 VENCEU')
elif jogador1 == 3 and jogador2 == 1:
    print('JOGADOR 2 VENCEU')
elif jogador1 == 3 and jogador2 == 2:
    print('JOGADOR 1 VENCEU')
