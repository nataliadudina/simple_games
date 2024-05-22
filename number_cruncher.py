import random


def get_limit_number(limit):
    """Получение правой границы диапозона и проверка числа"""
    while True:
        if not is_valid(limit):
            print(f'А может быть все-таки введем целое положительное число?')
            limit = input()
        else:
            print(f'Отлично! Угадываем число от 1 до {limit}.')
            return limit


def is_valid(n):
    """Защита от дураков."""
    if n.isdigit():
        return True
    return False


def game():
    """Ход игры, генерация случайного числа, подсчёт попыток."""
    user_number = input('Введите положительное целое число, чтобы установить диапозон игры от 1 до ...\n')
    choice_limit = int(get_limit_number(user_number))

    number_to_guess = random.randint(1, choice_limit)
    attempts = 0

    while True:
        num = input('Введите целое число: ')
        if not is_valid(num) or not 1 <= int(num) <= choice_limit:
            print(f'А может введем-таки целое число от 1 до {choice_limit}?')
        elif is_valid(num) and 1 <= int(num) <= choice_limit:
            if int(num) < int(number_to_guess):
                print('Ваше число меньше загаданного, попробуйте еще разок.')
                attempts += 1
            elif int(num) > int(number_to_guess):
                print('Ваше число больше загаданного, попробуйте еще разок.')
                attempts += 1
            elif int(num) == int(number_to_guess):
                attempts += 1
                print(f'Поздравляем! Вы угадали с {attempts} попытки.')
                break
    new_game()


def new_game():
    """Запрос на новый раунд"""
    answer = input('Спасибо, что играли в числовую угадайку. Хотите сыграть ещё раз? Да / Нет.\n').lower()

    if answer == 'да':
        print()
        game()
    else:
        print('Хорошо. Увидимся позже!')


# основная программа
print('Добро пожаловать в числовую угадайку.')

game()
