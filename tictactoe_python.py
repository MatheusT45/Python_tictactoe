#!/usr/bin/env python
# coding: utf-8

#Seja Bem-Vindo ao meu primeiro projeto em Python! Essa foi minha primeira vez experimentando essa linguagem incrível.


from IPython.display import clear_output
#define numero de jogadas
jogadas = 1
#define o tabuleiro vazio
board = []
for i in range(1,11):
        board+= ' '
#funcao para visualizacao da tela
def display():
    global board
    print('  '+board[7]+' | '+board[8]+' | '+board[9]+'')
    print('-------------')
    print('  '+board[4]+' | '+board[5]+' | '+board[6]+'')
    print('-------------')
    print('  '+board[1]+' | '+board[2]+' | '+board[3]+'')
    

#zera as jogadas e o tabuleiro
def clear_board():
    global board
    global jogadas
    board = []
    for i in range(1,11):
        board+= ' '
    jogadas = 1
    print('Tabuleiro Limpo')
    

#inicia o jogo
def play_():
    global jogadas
    global board
    
    display()
    #input do local
    local = input('Insira o local da sua jogada: ')
    clear_output()
    try:
        local = int(local)
    except:
        print('Local inválido')
        play_()
        
    #defininado o jogador
    if jogadas % 2 == 0:
        jogador = 'O'
    else:
        jogador = 'X'
        
    #verificando se o local está vazio e armazenando o jogador nele
    if  1 <= local <=9:
        if board[local] == ' ':
            board[local] = jogador
        else:
            print('Alguem já jogou nesse lugar')
            play_()
    else:
        print('Local Inválido')

    
    print('Número de jogadas: ', jogadas)

    #incrementa numero de jogadas
    jogadas+=1
   
    #decide se o jogador venceu na jogada
    decide_vencedor(jogador)
    
#funcao para verificar se o jogador venceu a partida
def decide_vencedor(jogador):
    global board
    #jogadas horizontais
    if board[7] == board[8] == board[9] == 'X' or board[7] == board[8] == board[9] == 'O':
        mensagem = 'Jogador '+jogador+' venceu a partida!'
        display()
        de_novo(mensagem)
    elif board[4] == board[5] == board[6] == 'X' or board[4] == board[5] == board[6] == 'O':
        mensagem = 'Jogador '+jogador+' venceu a partida!'
        display()
        de_novo(mensagem)
    elif board[1] == board[2] == board[3]  == 'X' or board[1] == board[2] == board[3]  == 'O':
        mensagem = 'Jogador '+jogador+' venceu a partida!'
        display()
        de_novo(mensagem)
    #jogadas verticais
    elif board[7] == board[4] == board[1] == 'X' or board[7] == board[4] == board[1] == 'O':
        mensagem = 'Jogador '+jogador+' venceu a partida!'
        display()
        de_novo(mensagem)
    elif board[8] == board[5] == board[2] == 'X' or board[8] == board[5] == board[2] == 'O':
        mensagem = 'Jogador '+jogador+' venceu a partida!'
        display()
        de_novo(mensagem)
    elif board[9] == board[6] == board[3] == 'X' or board[9] == board[6] == board[3] == 'O':
        mensagem = 'Jogador '+jogador+' venceu a partida!'
        display()
        de_novo(mensagem)
    #jogadas diagonais
    elif board[1] == board[5] == board[9] == 'X' or board[1] == board[5] == board[9] == 'O':
        mensagem = 'Jogador '+jogador+' venceu a partida!'
        display()
        de_novo(mensagem)
    elif board[7] == board[5] == board[3] == 'X' or board[7] == board[5] == board[3] == 'O':
        mensagem = 'Jogador '+jogador+' venceu a partida!'
        display()
        de_novo(mensagem)
    #empate
    elif board[9] != ' ' and board[8] != ' ' and board[7] != ' ' and board[7] != ' ' and board[6] != ' ' and board[5] != ' ' and board[4] != ' ' and board[3] != ' ' and board[2] != ' ' and board[1] != ' ':  
        mensagem = 'Empate!'
        display()
        de_novo(mensagem)
    else:
        play_()

#decisao de jogar novamente do jogador
def de_novo(mensagem): 
    global jogadas
    print(mensagem)
    pergunta = input('Jogar novamente? ')
    if pergunta == 'sim':
        jogadas = 1
        clear_board()
        clear_output()
        play_()
    else:
        clear_board()
        print('Obrigado por jogar!')





