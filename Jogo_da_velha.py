import os
import time
from colorama import Fore
import tkinter as tk
from tkinter import ttk
try:
    jogarNovamente = "s"
    jogadas = 0
    quemJoga = 1
    qtdePlayers = 0
    vit = "n"
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    cls = lambda: os.system('cls')
    pause = lambda: os.system('Pause')
    #-----------------------------------------------------------------------------------------------------
    #inteligencia minimax
    def is_board_full(board):
        for row in board:
            if " " in row:
                return False
        return True

    def check_winner(board, player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
            if all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def get_available_moves(board):
        available_moves = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    available_moves.append(row * 3 + col)
        return available_moves

    def minimax(board, depth, is_maximizing, alpha, beta):
        if check_winner(board, "X"):
            return -10 + depth
        if check_winner(board, "O"):
            return 10 - depth
        if is_board_full(board):
            return 0
        
        if is_maximizing:
            max_eval = -float("inf")
            for move in get_available_moves(board):
                board[move // 3][move % 3] = "O"
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[move // 3][move % 3] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float("inf")
            for move in get_available_moves(board):
                board[move // 3][move % 3] = "X"
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[move // 3][move % 3] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def find_best_move(board):
        best_move = -1
        best_eval = -float("inf")
        for move in get_available_moves(board):
            board[move // 3][move % 3] = "O"
            eval = minimax(board, 0, False, -float("inf"), float("inf"))
            board[move // 3][move % 3] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move

    def cpuJoga():
        global jogadas
        global quemJoga
        if quemJoga == 2 and jogadas < 9:
            print("Aguarde, estou pensando...")
            time.sleep(2)

            best_move = find_best_move(velha)
            l, c = best_move // 3, best_move % 3

            velha[l][c] = "O"
            quemJoga = 1
            jogadas += 1
    #-----------------------------------------------------------------------------------------------------
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def tela():
        global velha
        global jogadas
        clear_screen()
        print("   0   1   2")
        i = 0
        while i < 3:
            print(f'{i}:  ' + velha[i][0] + ' | ' + velha[i][1] + ' | ' + velha[i][2])
            print("   -----------")
            i += 1
        print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

    
    
    def jogador1Joga(l, c):
        global jogadas
        global quemJoga
        if quemJoga == 1 and jogadas < 9:
            try:
                if velha[l][c] != " ":
                    print("Posição inválida, digite novamente.")
                else:
                    velha[l][c] = "X"
                    quemJoga = 2
                    jogadas += 1
            except:
                print("Jogada inválida")
                pause()
        tela()


    def jogador2Joga(l, c):
        global jogadas
        global quemJoga
        if quemJoga == 2 and jogadas < 9:
            try:
                if velha[l][c] != " ":
                    print("Posição inválida, digite novamente.")
                else:
                    velha[l][c] = "O"
                    quemJoga = 1
                    jogadas += 1
            except:
                print("Jogada inválida")
                pause()
        tela()

    def verificaVitoria():
        global velha
        vitoria = "n"
        simbolos = ["X", "O"]
        for s in simbolos:
            vitoria = "n"
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
            ic = 0
            while ic < 3:
                soma = 0
                il = 0
                while il < 3:
                    if velha[il][ic] == s:
                        soma += 1
                    il += 1
                if soma == 3:
                    vitoria = s
                    break
                ic += 1
            if (vitoria != "n"):
                break
            soma = 0
            idiag = 0
            while idiag < 3:
                if (velha[idiag][idiag] == s):
                    soma += 1
                idiag += 1
            if (soma == 3):
                vitoria = s
                break
            soma = 0
            idiagL = 0
            idiagC = 2
            while idiagL >= 0 and idiagL <= 2:
                if (velha[idiagL][idiagC] == s):
                    soma += 1
                idiagL += 1
                idiagC -= 1
            if (soma == 3):
                vitoria = s
                break
        return vitoria

    def redefinir():
        global velha
        global jogadas
        global quemJoga
        global vit
        jogadas = 0
        quemJoga = 2
        vit = "n"
        velha = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
    def jogo():
        global jogarNovamente
        while jogarNovamente == "s":
            clear_screen()
            print("-*-*-*-*-*-*-*-*-*-*-JOGO DA VELHA-*-*-*-*-*-*-*-*-*-*-")
            print("Jogar contra CPU [1]")
            print("Jogar contra Amigo [2]")
            qtdPlayers = int(input("Escolha [1/2]: "))
            if (qtdPlayers != 1 and qtdPlayers != 2):
                print("Quantidade de jogadores invalida.")
                jogarNovamente = input("Jogar Novamente? [s/n]")
                redefinir()
#--------------------------------------------------------------------
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
                jogarNovamente = input(Fore.BLUE + "Jogar Novamente? [s/n]: " + Fore.RESET)
                jogarNovamente = jogarNovamente.lower()
                redefinir()
except Exception as e:
    print(e)

janela = tk.Tk()
#codigo front-end aqui-------------------------------------------------------------------
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0,weight=1)
janela.title("Jogo da Velha")

#configuracoes de titulo-----------------------------------------------------------------
titulo = tk.Label(text="Jogo da Velha", fg='Black', bg='#FF00FF', width=35, height=5)
titulo.grid(row=0, column=0, columnspan=4, sticky="EW")

#configuracoes de quantidade de jogadores-----------------------------------------------------------------
quantidadeJogadores = tk.Label(text="Quantidade de Jogadores", fg='Black', bg='white')
quantidadeJogadores.grid(row=1, column=0)

dicionario_Players = {
    'Jogador Vs CPU': 1,
    'Jogador Vs Jogador': 2
}
jogadores = list(dicionario_Players.keys())

jogador = ttk.Combobox(janela, values=jogadores)
jogador.grid(row=1, column=1)

def setQdtePlayers():
    global qtdePlayers
    qtdePlayers = int(dicionario_Players.get(jogador.get()))
    print(qtdePlayers)
    jogador.set("")



botaoSetJogadores = tk.Button(text="Set", command=setQdtePlayers)
botaoSetJogadores.grid(row=1, column=2,columnspan=2, sticky="EW")

#configurações do jogador 1-----------------------------------------------------------
jogador1 = tk.Label(text="Jogador 1: ", fg='Black', bg='white')
jogador1.grid(row=2, column=0)

movesL= [0,1,2]
movesC= [0,1,2]

l1 = ttk.Combobox(janela, values=movesL)
l1.grid(row=2, column=1)
c1 = ttk.Combobox(janela, values=movesC)
c1.grid(row=2, column=2)
l1.set("Escolha a Linha")
c1.set("Escolha a Coluna")

def jogadaJogador1():
    linha1 = int(l1.get())
    coluna1= int(c1.get())
    print(f"Linha.: {linha1}")
    print(f"Coluna: {coluna1}")
    l1.set("")
    c1.set("")
    jogador1Joga(linha1,coluna1)


botaoSetjogadaJogador1 = tk.Button(text="Set", command=jogadaJogador1)
botaoSetjogadaJogador1.grid(row=2, column=3)

#configurações do jogador 2-----------------------------------------------------------
jogador2 = tk.Label(text="Jogador 2: ", fg='Black', bg='white')
jogador2.grid(row=3, column=0)

movesL= [0,1,2]
movesC= [0,1,2]

l2 = ttk.Combobox(janela, values=movesL)
l2.grid(row=3, column=1)
c2 = ttk.Combobox(janela, values=movesC)
c2.grid(row=3, column=2)
l2.set("Escolha a Linha")
c2.set("Escolha a Coluna")

def jogadaJogador2():
    linha2 = int(l2.get())
    coluna2= int(c2.get())
    print(f"Linha.: {linha2}")
    print(f"Coluna: {coluna2}")
    l2.set("")
    c2.set("")
    jogador2Joga(linha2,coluna2)


botaoSetjogadaJogador1 = tk.Button(text="Set", command=jogadaJogador2)
botaoSetjogadaJogador1.grid(row=3, column=3)


janela.mainloop()






