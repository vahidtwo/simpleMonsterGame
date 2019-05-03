import os
import random

CELLS = [
(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
(0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
(0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
(0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
]
def get_locatios():
    return random.sample(CELLS,3)

def move_player(player, move):
    x, y = player
    if move=='LEFT':
        x-=1
    if move=='RIGHT':
        x+=1
    if move=='UP':
        y-=1
    if move=='DOWN':
        y+=1
    return x, y

def get_move(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player
    if x == 0:
        moves.remove('LEFT')
    if x == 4:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == 4:
        moves.remove('DOWN')
    return moves

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def draw_map(player):
    print(' _'*5)
    tile = '|{}'
    for cell in CELLS:
        x, y = cell
        if x < 4 :
            line_end = ''
            if cell == player:
                output = tile.format('X')
            else:
                output = tile.format("_")
        else:
            line_end = '\n'
            if cell == player :
                output = tile.format('X|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)

def main():
    monster, player, door = get_locatios()
    MOVE_LIST = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    while True:
        valid_move = get_move(player)
        if player == monster:
            print('monster kill you')
            break
        elif player == door:
            print('*****************you win******************')
            break
        else:
            print('welcome to my Game')
            draw_map(player)
            print('if you want exit type `quit`')
            print('you are in room {}'.format(player))
            print('your move is {}'.format(', '.join(valid_move)))
            #print('monster {}, door {}'.format(monster,door))

            move = input('> ')
            if move =='w':
                move = 'UP'
            if move =='s':
                move = 'DOWN'
            if move =='d':
                move = 'RIGHT'
            if move =='a':
                move = 'LEFT'
            move = move.upper()
            clear_screen()
            if move =='QUIT':
                break
            if move in valid_move:
                player = move_player(player, move)
            else:
                if move in MOVE_LIST:
                    print('you cant go inside de walls :)')
                    continue
                else:
                    print('you type in chertopert style')
    ret = input('\nare you want play again ANY/Y\n')
    if ret.upper() == 'Y':
        clear_screen()
        main()
    else:
        print ('bye')

main()