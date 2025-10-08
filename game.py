import random

while True:
    game_count = 0
    player_win = 0
    player_lose = 0
    pc_number = random.randint(1, 100)

    while game_count < 5:
        game_count += 1
        print(f"\n Попытка {game_count} из 5")
        while True:
            player_number = int(input(f'\nПопытка {game_count}/5. Введите число от 1 до 100: '))
            if player_number in range(1, 101):
                break
            else:
                print('число должно быть от 1 до 100!!!')
        if player_number == pc_number:
            print('вы молодец!')
            player_win += 1
            break
        elif player_number > pc_number:
            print('загаднное число меньше')
        elif player_number < pc_number:
            print('загаданное число больше')
    if player_win == 0:
        print(f'\nВы проиграли! Я загадал число: {pc_number}')
        player_lose = 1
    print(f"\nИГРА ОКОНЧЕНА")
    print(f"Загаданное число: {pc_number}")
    print(f"Попыток использовано: {game_count}")
    if player_win == 1:
        print("Результат: ПОБЕДА! ")
    else:
        print("Результат: ПРОИГРЫШ ")

    again = input("введите 1 если хотите сыграть еще раз: ")
    if again != "1":
        break
    print()
