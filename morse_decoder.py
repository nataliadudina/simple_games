import random

morse_letters = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
                 "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
                 "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
                 "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}

animals = ['cat', 'rat', 'dog', 'pig', 'tiger']
nature = ['rain', 'fog', 'wind', 'tree', 'grass']

# списки с вариантами реакций на ответ пользователя
right_answers = ['Correct!', 'Well done!', 'Good job!', 'That\'s right!', 'You rock!', 'Success!']
wrong_answers = ['Nope.', 'Oops, missed guess.', 'Error detected.', 'Incorrect.',
                 'Ouch, try harder.', 'Mistakes happen.']


def is_invalid(choice: str):
    """
    Валидация выбора пользователя.
    """
    if choice != 'a' and choice != 'n':
        return True
    return False


def get_word(words):
    """
    Получение случайного слова из игрового списка.
    """
    return random.choice(words)


def morse_encode(random_word: str):
    """
    Кодирование случайного слова из игрового списка.
    """
    morse_word = ''
    for letter in random_word:
        sign = morse_letters.get(letter)
        morse_word += sign
    return morse_word


def get_right_answer():
    """
    Выбор случайной реакции при верном ответе.
    """
    random.shuffle(right_answers)
    feedback = right_answers[0]
    return feedback


def get_wrong_answer():
    """
    Выбор случайной реакции при неверном ответе.
    """
    index = random.randint(0, len(wrong_answers) - 1)
    feedback = wrong_answers[index]
    return feedback


def print_statistics(answers):
    """
    Вывод статистики верных и неверных ответов.
    """
    right = answers.count(True)
    wrong = answers.count(False)
    print(f'Right answers: {right}')
    print(f'Wrong answers: {wrong}')


def main():
    # основная программа

    answers = []

    morse_list = []

    # старт игры и выбор списка слов
    input('Today we will practice deciphering Morse code. Press Enter to start.')
    user_choice = input('Choose the topic: animals or nature. Print A or N.\n').lower()

    while is_invalid(user_choice):
        user_choice = input('Please, choose the topic: animals or nature. Print A or N.\n').lower()

    print('Great! The choice is made. Let\'s play!')
    print(f'Here is a prompt if needed:')
    print("""
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", \n
    "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",\n
     "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", \n
    "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
    """)

    print()

    # создание игрового списка
    if user_choice == 'a':
        morse_list = animals
    else:
        morse_list = nature

    # запуск игры с количеством заданий равным длине игрового списка
    for i in range(len(morse_list)):
        word = get_word(morse_list)
        user_answer = input(f'Word {i+1}: {morse_encode(word)} \n{len(word)} letters.\nYour answer - ')
        if user_answer == word:
            print(f'{get_right_answer()} It is {word}.')
            answers.append(True)
        else:
            print(f'{get_wrong_answer()} It is {word}.')
            answers.append(False)
        print()

    # окончание игры, вывод статистики
    print(f'Well, that is all. High five! \nTotal words: {len(morse_list)}')
    print_statistics(answers)


if __name__ == '__main__':
    main()
