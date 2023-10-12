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

            best_move = find_best_move(velha)
            l, c = best_move // 3, best_move % 3

            velha[l][c] = "O"
            atualizar_campos()
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

    def atualizar_campos():
        campo00.config(text="     " + f"{velha[0][0]}")
        campo01.config(text=f"{velha[0][1]}"+"    ")
        campo02.config(text=f"{velha[0][2]}")

        campo10.config(text="     " + f"{velha[1][0]}")
        campo11.config(text=f"{velha[1][1]}"+"    ")
        campo12.config(text=f"{velha[1][2]}")

        campo20.config(text="     " + f"{velha[2][0]}")
        campo21.config(text=f"{velha[2][1]}"+"    ")
        campo22.config(text=f"{velha[2][2]}")

    def jogador1Joga(l, c):
        global jogadas
        global quemJoga
        if quemJoga == 1 and jogadas < 9:
            try:
                if velha[l][c] != " ":
                    print("Posição inválida, digite novamente.")
                else:
                    velha[l][c] = "X"
                    atualizar_campos()
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
                    atualizar_campos()
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
            
except Exception as e:
    print(e)

fonte_personalizada = ("Arial", 16)
fonte_personalizadaT = ("Arial", 20)
fonte_personalizadaC = ("Arial", 50)

janela = tk.Tk()
#codigo front-end aqui-------------------------------------------------------------------
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0,weight=1)
janela.configure(bg="white")
janela.title("Jogo da Velha")
#configuracoes de titulo-----------------------------------------------------------------
titulo = tk.Label(text="Jogo da Velha", fg='Black', bg='#FF00FF', width=35, height=5,font=fonte_personalizadaT)
titulo.grid(row=0, column=0, columnspan=7, sticky="NEW")


#Criar separador vertical
separator = ttk.Separator(janela, orient="vertical")
separator.grid(row=1, column=1, rowspan=15, sticky="NS")  # Preenchimento vertical

#configuracoes de quantidade de jogadores-----------------------------------------------------------------
quantidadeJogadores = tk.Label(text="Quantidade de Jogadores:", fg='Black', bg='white',font=fonte_personalizada)
quantidadeJogadores.grid(row=1, column=0, sticky="nsew")

dicionario_Players = {
    'Jogador Vs CPU': 1,
    'Jogador Vs Jogador': 2
}
jogadores = list(dicionario_Players.keys())

jogador = ttk.Combobox(janela, values=jogadores)
jogador.grid(row=1, column=2, sticky="nsew")

def setQdtePlayers():
    global qtdePlayers
    qtdePlayers = int(dicionario_Players.get(jogador.get()))
    print(qtdePlayers)
    jogador.set("")



botaoSetJogadores = tk.Button(text="Set", command=setQdtePlayers)
botaoSetJogadores.grid(row=1, column=3,columnspan=5, sticky="NSEW")

# Criar um ttk.Separator
separator = ttk.Separator(janela, orient="horizontal")
separator.grid(row=2, column=0, columnspan=7, sticky="EW")  # Preenchimento horizontal

#configurações do jogador 1-----------------------------------------------------------
jogador1 = tk.Label(text="Jogador 1: ", fg='Black', bg='white',font=fonte_personalizada)
jogador1.grid(row=3, column=0, sticky="EW")

movesL= [0,1,2]
movesC= [0,1,2]

l1 = ttk.Combobox(janela, values=movesL)
l1.grid(row=3, column=2)
c1 = ttk.Combobox(janela, values=movesC)
c1.grid(row=3, column=3)
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
    if qtdePlayers == 1 and quemJoga == 2:
        CPUtxt.config(text="Aguarde estou pensando.")
        jogadaCPU()

botaoSetjogadaJogador1 = tk.Button(text="Set", command=jogadaJogador1)
botaoSetjogadaJogador1.grid(row=3, column=4,columnspan=3,sticky="EW")

# Criar um ttk.Separator
separator = ttk.Separator(janela, orient="horizontal")
separator.grid(row=4, column=0, columnspan=7, sticky="EW")  # Preenchimento horizontal

#configurações do jogador 2-----------------------------------------------------------
jogador2 = tk.Label(text="Jogador 2: ", fg='Black', bg='white',font=fonte_personalizada)
jogador2.grid(row=5, column=0, sticky="EW")

movesL= [0,1,2]
movesC= [0,1,2]

l2 = ttk.Combobox(janela, values=movesL)
l2.grid(row=5, column=2)
c2 = ttk.Combobox(janela, values=movesC)
c2.grid(row=5, column=3)
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


botaoSetjogadaJogador2 = tk.Button(text="Set", command=jogadaJogador2)
botaoSetjogadaJogador2.grid(row=5, column=4,columnspan=3,sticky="EW")

# Criar um ttk.Separator
separator = ttk.Separator(janela, orient="horizontal")
separator.grid(row=6, column=0, columnspan=7, sticky="EW")  # Preenchimento horizontal


#configurações do CPU-----------------------------------------------------------
CPU = tk.Label(text="CPU: ", fg='Black', bg='white',font=fonte_personalizada)
CPU.grid(row=7, column=0)

CPUtxt=tk.Label(fg='Black', bg='white')
CPUtxt.grid(row=7, column=2, columnspan=5, sticky="EW")

def jogadaCPU():
        time.sleep(2)
        cpuJoga()
        
        



# Criar um ttk.Separator
separator = ttk.Separator(janela, orient="horizontal")
separator.grid(row=8, column=0, columnspan=7, sticky="EW")  # Preenchimento horizontal
    
#Configurações de tela:--------------------------------------------------
x0 = tk.Label(text="            ", fg='white', bg='Black',width=20,height=5,font=fonte_personalizada)#coluna 0
x0.grid(row=9, column=0, columnspan=2)

separator = ttk.Separator(janela, orient="horizontal")
separator.grid(row=10, column=0, columnspan=6, sticky="EW")  # Preenchimento horizontal

co0 = tk.Label(text="0            ", fg='white', bg='Black',width=25,height=5,font=fonte_personalizada)#coluna 0
co0.grid(row=9, column=2,columnspan=2,sticky="EW")

separator = ttk.Separator(janela, orient="vertical")
separator.grid(row=9, column=3, rowspan=7, sticky="NS")  # Preenchimento vertical

co1 = tk.Label(text="1            ", fg='white', bg='Black',width=10,height=5,font=fonte_personalizada)#coluna 1
co1.grid(row=9, column=4,sticky="EW")

separator = ttk.Separator(janela, orient="vertical")
separator.grid(row=9, column=5, rowspan=7, sticky="NS")  # Preenchimento vertical

co2 = tk.Label(text="2", fg='white', bg='Black', width=17,height=5,font=fonte_personalizada)#coluna 2
co2.grid(row=9, column=6,sticky="EW")

li0 = tk.Label(text="0", fg='white', bg='Black',width=20,height=5,font=fonte_personalizada)#linha 0
li0.grid(row=11, column=0,sticky="NS")

separator = ttk.Separator(janela, orient="horizontal")
separator.grid(row=12, column=0, columnspan=7, sticky="EW")  # Preenchimento horizontal

li1 = tk.Label(text="1", fg='white', bg='Black',width=20,height=5,font=fonte_personalizada)#linha 1
li1.grid(row=13, column=0,sticky="NS")

separator = ttk.Separator(janela, orient="horizontal")
separator.grid(row=14, column=0, columnspan=7, sticky="EW")  # Preenchimento horizontal

li2 = tk.Label(text="2", fg='white', bg='Black', width=20,height=5,font=fonte_personalizada)#linha 2
li2.grid(row=15, column=0,sticky="NS")
    #-------------------------------------------------CAMPOS-------------------------------------------------------------------------------------------
campo00=tk.Label(fg='black', bg='white',width=2,height=1,font=fonte_personalizadaC)#Campo00
campo00.grid(row=11,column=2,columnspan=1,sticky="NSEW")

campo01=tk.Label(fg='black', bg='white',width=2,height=1,font=fonte_personalizadaC)#Campo01
campo01.grid(row=11,column=4,sticky="NSEW")

campo02=tk.Label(fg='black', bg='white',width=2,height=1,font=fonte_personalizadaC)#Campo02
campo02.grid(row=11,column=6,sticky="NSEW")

campo10=tk.Label(fg='black', bg='white',width=2,height=1,font=fonte_personalizadaC)#Campo10
campo10.grid(row=13,column=2,columnspan=1,sticky="NSEW")

campo11=tk.Label(fg='black', bg='white',width=2,height=1,font=fonte_personalizadaC)#Campo01
campo11.grid(row=13,column=4,sticky="NSEW")

campo12=tk.Label(fg='black', bg='white',width=2,height=1,font=fonte_personalizadaC)#Campo02
campo12.grid(row=13,column=6,sticky="NSEW")

campo20=tk.Label(fg='black', bg='white',width=2,height=1,font=fonte_personalizadaC)#Campo20
campo20.grid(row=15,column=2,columnspan=1,sticky="NSEW")

campo21=tk.Label(fg='black', bg='white',width=2,height=1,font=fonte_personalizadaC)#Campo21
campo21.grid(row=15,column=4,sticky="NSEW")

campo22=tk.Label(fg='black', bg='white',width=2,height=1,font=fonte_personalizadaC)#Campo22
campo22.grid(row=15,column=6,sticky="NSEW")

janela.mainloop()






