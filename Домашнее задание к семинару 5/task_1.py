# Создайте программу для игры с конфетами человек против человека.
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#     Первый ход определяется жеребьёвкой.
#     За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#     Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота
#     b) Подумайте как наделить бота ""интеллектом""

from random import randint as ri

total_sweet = int(input('введите количество конфет на столе: '))
take_sweet = 0
pleer_sweet = 0
bot_sweet = 0


def whe_is_first():
        random_number = ri(1,2)
        if random_number == 1:
            pleer_turn()
        else:
            bot_turn()

def pleer_turn():
        global total_sweet
        global take_sweet
        global pleer_sweet
        print(f'Ваш ход, сейчас на столе {total_sweet} конфет')
        take_sweet = int(input('Сколько конфет вы хотите взять? '))
        while take_sweet > 28 or take_sweet < 0  or take_sweet > total_sweet:
            take_sweet = int(input('Вы берёте слмшком много конфет! Попробуйте снова '))
        total_sweet -= take_sweet
        pleer_sweet += take_sweet
        if total_sweet > 0:
            bot_turn()
        else:
            print('Вы победили!')

def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(1, 28)
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    print(f'Бот взял {take_sweet} конфет! На столе осталоь {total_sweet} конфет!')
    if total_sweet > 0:
        pleer_turn()
    else:
        print('Бот победил!')

whe_is_first()