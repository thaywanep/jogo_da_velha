def novoTabuleiro():
    return [0, 0, 0,
            0, 0, 0,
            0, 0, 0]
def imprimirTabuleiro(tabuleiro):
    for indice, valor in enumerate(tabuleiro):
        if valor == 0:
            print(' ', indice + 1, sep='', end='')
        elif valor == 1:
            print(' X', end='')
        else:
            print(' O', end='')

        if indice == 2 or indice == 5:
            print('\n---+---+---\n', end='')
        elif indice < 8:
            print(' |', end='')
    print('\n')

def recebeJogada(jogador):
    try:
        jogada = int(input('Digite a posição a Jogar 1-9 (jogador %s): ' % jogador))
        return jogada
    except ValueError:
        print('Entrada Inválida')
        return -1

def posiçãoValida(jogada, tabuleiro):
    if jogada < 1 or jogada > 9:
        print('Posição Inválida')
        return False
    if tabuleiro[jogada - 1] != 0:
        print('Posição Ocupada')
        return False
    return True

def mudaJogador(jogador, jogada, tabuleiro):
    if jogador == 'X':
        tabuleiro[jogada - 1] = 1
        return 'O'
    else:
        tabuleiro[jogada - 1] = 2
        return 'X'

def verificaFimDeJogo(numJogadas, tabuleiro):
    #verifica linhas
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
        if tabuleiro[0] == 1:
            print('Jogador X Ganhou!')
            return 1
        elif tabuleiro[0] == 2:
            print('Jogador O Ganhou!')
            return 2
    if tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
        if tabuleiro[3] == 1:
            print('Jogador X Ganhou!')
            return 1
        elif tabuleiro[3] == 2:
            print('Jogador O Ganhou!')
            return 2
    if tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
        if tabuleiro[6] == 1:
            print('Jogador X Ganhou!')
            return 1
        elif tabuleiro[6] == 2:
            print('Jogador O Ganhou!')
            return 2
    #verifica colunas
    if tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
        if tabuleiro[0] == 1:
            print('Jogador X Ganhou!')
            return 1
        elif tabuleiro[0] == 2:
            print('Jogador O Ganhou!')
            return 2
    if tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
        if tabuleiro[1] == 1:
            print('Jogador X Ganhou!')
            return 1
        elif tabuleiro[1] == 2:
            print('Jogador O Ganhou!')
            return 2
    if tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
        if tabuleiro[2] == 1:
            print('Jogador X Ganhou!')
            return 1
        elif tabuleiro[2] == 2:
            print('Jogador O Ganhou!')
            return 2
    #verifica diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
        if tabuleiro[0] == 1:
            print('Jogador X Ganhou!')
            return 1
        elif tabuleiro[0] == 2:
            print('Jogador O Ganhou!')
            return 2
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        if tabuleiro[2] == 1:
            print('Jogador X Ganhou!')
            return 1
        elif tabuleiro[2] == 2:
            print('Jogador O Ganhou!')
            return 2
    if numJogadas >= 9:
        print('Deu Velha!')
        return -1
    return 0

############################################
#Implementação

tabuleiro = novoTabuleiro()

jogador = 'X'
jogadas = 0

while True:
    imprimirTabuleiro(tabuleiro)
    jogada = recebeJogada(jogador)
    if not posiçãoValida(jogada, tabuleiro):
        continue
    jogador = mudaJogador(jogador, jogada, tabuleiro)
    jogadas += 1
    if verificaFimDeJogo(jogadas, tabuleiro) != 0:
        break
