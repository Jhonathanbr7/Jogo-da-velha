import os
import random
import time
from colorama import Fore

jogarNovamente = "s"
jogadas = 0
quemJoga = 1
vit = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

cls = lambda: os.system('cls')
pause = lambda: os.system('Pause')


def tela():
    global velha
    global jogadas
    cls()
    print("   0   1   2")
    i = 0
    while i < 3:
        print(f'{i}:  ' + velha[i][0] + ' | ' + velha[i][1] + ' | ' + velha[i][2])
        print("   -----------")
        i += 1
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)


def jogador1Joga():
    global jogadas
    global quemJoga
    if quemJoga == 1 and jogadas < 9:
        try:
            l = int(input("Linha..:"))
            c = int(input("Coluna.:"))
            while velha[l][c] and velha[l][c] != " ":
                print("Posição invalida, digite novamente.")
                l = int(input("Linha..:"))
                c = int(input("Coluna.:"))
            velha[l][c] = "X"
            quemJoga = 2  # passa a vez pro jogador2
            jogadas += 1
        except:
            print("Jogada invalida")
            pause()


def jogador2Joga():
    global jogadas
    global quemJoga
    if quemJoga == 2 and jogadas < 9:
        try:
            l = int(input("Linha..:"))
            c = int(input("Coluna.:"))
            while velha[l][c] != " ":
                print("Posição invalida, digite novamente.")
                l = int(input("Linha..:"))
                c = int(input("Coluna.:"))
            velha[l][c] = "O"
            quemJoga = 1  # passa a vez pro jogador1
            jogadas += 1
        except:
            print("Jogada invalida")
            pause()


def cpuJoga():  # jogadas da cpu geradas de forma aleátoria
    global jogadas
    global quemJoga
    if quemJoga == 2 and jogadas < 9:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        print("Aguarde, estou pensando...")  # adição divertida ao codigo
        time.sleep(4)                        # atraso para dar a sensação de uma partida real
        velha[l][c] = "O"
        quemJoga = 1  # passa a vez pro jogador1
        jogadas += 1


def verificaVitoria():  # verifica vitoria em todos os metodos possiveis (linhas,colunas, diagonais) a ausência de vitoria, pressupoe empate.
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"

        # verifica vitoria em linhas
        il = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (velha[il][ic] == s):
                    soma += 1
                ic += 1
            if (soma == 3):
                vitoria = s
                break
            il += 1
        if (vitoria != "n"):
            break

        # verifica vitoria em colunas
        ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if (velha[il][ic] == s):
                    soma += 1
                il += 1
            ic += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != "n"):
            break

        # verifica diagonal principal
        soma = 0
        idiag = 0
        while idiag < 3:
            if (velha[idiag][idiag] == s):
                soma += 1
            idiag += 1
        if (soma == 3):
            vitoria = s
            break

        # verifica diagonal secundaria
        soma = 0
        idiagL = 0  # indice linha da diagonal
        idiagC = 2  # indice coluna da diagonal
        while idiagL >= 0 and idiagL <= 2:
            if (velha[idiagL][idiagC] == s):
                soma += 1
            idiagL += 1
            idiagC -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria


def redefinir():  # Redefine todas as variaveis globais quando chamado.
    global velha
    global jogadas
    global quemJoga
    global vit

    jogadas = 0
    quemJoga = 1
    vit = "n"
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


while jogarNovamente == "s":
    print("-*-*-*-*-*-*-*-*-*-*-JOGO DA VELHA-*-*-*-*-*-*-*-*-*-*-")
    print("Jogar contra CPU [1]")
    print("Jogar contra Amigo [2]")
    qtdPlayers = int(input("Escolha [1/2]: "))
    if (qtdPlayers != 1 and qtdPlayers != 2):
        print("Quantidade de jogadores invalida.")
        jogarNovamente = input("Jogar Novamente? [s/n]")
        redefinir()
    if (qtdPlayers == 1 or qtdPlayers == 2):
        while True:
            tela()
            print(Fore.CYAN + "Jogador 1" + Fore.RESET)
            jogador1Joga()
            tela()
            vit = verificaVitoria()
            if (vit != "n" or jogadas >= 9):
                break
            print(Fore.CYAN + "Jogador 2" + Fore.RESET)
            if (qtdPlayers == 1):
                cpuJoga()
            else:
                jogador2Joga()
            tela()
            vit = verificaVitoria()
            if (vit != "n" or jogadas >= 9):
                break
        print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW)
        if (vit == "X" or vit == "O"):
            print("Resultado: Jogador " + vit + " venceu" + Fore.RESET)
        else:
            print("Resultado: Empate" + Fore.RESET)
        jogarNovamente = input(Fore.BLUE + "Jogar Novamente? [s/n]" + Fore.RESET)
        redefinir()
