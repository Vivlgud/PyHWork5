# 3Создайте программу для игры в ""Крестики-нолики"".

# # area=[['.','.','.'] for i in range(3)]
# # print(area)

import random


def drawing_refresh(area):
    for i in area:
        print(i)
    print()


def find_position(pos):
    if pos == 1:
        area[0][0] = symbol
    elif pos == 2:
        area[0][1] = symbol
    elif pos == 3:
        area[0][2] = symbol
    elif pos == 4:
        area[1][0] = symbol
    elif pos == 5:
        area[1][1] = symbol
    elif pos == 6:
        area[1][2] = symbol
    elif pos == 7:
        area[2][0] = symbol
    elif pos == 8:
        area[2][1] = symbol
    elif pos == 9:
        area[2][2] = symbol


area = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
symbol1 = 'X'
symbol2 = '0'
drawing_refresh(area)


first_step = random.randint(1, 2)
if first_step == 1:
    symbol = symbol1
    print(f"первый игрок ставит '{symbol}'  \n")
    player = 1
else:
    symbol = symbol2
    print(f"первый игрок ставит {symbol}  \n")
    player = 2

busy_pos = []
pos_x=[]
pos_0=[]
for i in range(9):

    if player == 1:
        symbol = symbol1
        print(f'Ставим {symbol}')
        player = 2

    else:
        symbol = symbol2
        print(f'Ставим {symbol2}')
        player = 1

    pos = int(input("Введите цифру куда хотите поставить символ: "))

    while pos in busy_pos:
        print("Выбирете другую позицию")
        pos = int(input("Введите цифру куда хотите поставить символ: "))
    busy_pos.append(pos)
    if player==2:
        pos_x.append(pos)
    else:
        pos_0.append(pos)
    find_position(pos)
    drawing_refresh(area)

print(pos_x)
print(pos_0)

def winner(pos:list)->int:
    """Выявляет победителя"""

    win_player=0
    
    win_pos=((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
    for i in win_pos:
        count=0
        for j in i:
            for k in pos:
                if k==j:
                    count+=1
                if count==3:
                    win_player=1
                    return win_player
    return win_player               
                

win_x=winner(pos_x)
win_0=winner(pos_0)
if win_x>win_0:
    print(f"Победил игрок, ставящий Х")
elif win_x==win_0:
    print("Ничья")
else:
    print(f"Победил игрок, ставящий O")

