# 2 Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Если делаете a и b - не нужно создавать отдельных файлов с полностью копированным кодом, 
# лучше выделите в отдельные функции бота и умного бота.


print('*'*10+'Начало игры'+'*'*10)
print('-'*31+'\n')

game=int(input('Выберите цифру с кем будете играть: 1 - c другом, 2 - с ботом, 3 - со смарт ботом: '))

if game==1:
    player2=input("введите имя 2-го игрока: ")
elif game==2:
    player2='бот'
elif game==3:
    player2='SUPER бот'
else:
    print("Вы неправильно выбрали соперника. Перезапустите игру")
    import sys
    sys.exit()

player1=input("введите имя 1-го игрока: ")
konf=int(input('Введите начальное количество конфет: '))
max_konf=int(input('Введите максимальное количество конфет, которое можно взять за один ход: '))

def konf_game(player1:int,player2:int,konf:int,max_konf:int,game:int):
    import random
    first_step=random.randint(1,2)
    if first_step==1:
        print(f"первый ход делает {player1}  \n")
        player=1
    else:
        print(f"первый ход делает {player2}  \n")
        player=2


    while konf!=0:
        if player==1:
            print(f'Ход делает {player1}')
            win=1
            player=2
        else:
            print(f'Ход делает {player2}')
            win=2
            player=1
        if game==1:
            konf_step=int(input("Сколько конфет убираем: "))
        elif game==2 and player==2:
            konf_step=int(input("Сколько конфет убираем: "))
        elif game==2 and player==1:
            konf_step=random.randint(1,max_konf)
            print(f'Бот убрал {konf_step} конфет')
        elif game==3 and player==2:
            konf_step=int(input("Сколько конфет убираем: "))
        elif game==3 and player==1:
            konf_step=konf%(max_konf+1)
            if konf_step==0:
                konf_step=1
            print(f'SUPER бот убрал {konf_step} конфет')
        while konf_step>max_konf:
            print(f'Число не может быть больше {max_konf}')
            konf_step=int(input("Сколько конфет убираем: "))
        konf-=konf_step
        print(f'Осталось {konf} конфет')

    if win==1:
        print(f'Победил {player1}')
    else:
        print(f'Победил {player2}')

konf_game(player1,player2,konf,max_konf,game)
