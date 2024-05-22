words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "to believe": "верить",
    "to feel": "чувствовать",
    "to make": "делать",
    "to open": "открывать",
    "to think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "to suggest": "предлагать",
    "except": "кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}


def main():
    answers = {}
    words = {}

    choice = input('Привет! Проверим знание английских слов? \nВыбери уровень сложности. \nЛегкий (1), средний (2), '
                   'сложный (3).\nТвой выбор: ').strip().lower()
    if choice in ('легкий', '1'):
        words = words_easy
    elif choice in ('средний', '2'):
        words = words_medium
    elif choice in ('сложный', '3'):
        words = words_hard
    else:
        words = words_easy
        print('Похоже, ты сомневаешься в выборе. Давай начнём с легкого.\n')

    input('Уровень сложности выбран, напиши перевод для следующих 5 слов.\nНажми Enter, чтобы начать.')

    for word, meaning in words.items():
        print(f'{word}, {len(meaning)} букв, начинается на {meaning[0]}...')
        answer = input('Твой ответ: ')
        if answer == meaning:
            print(f'Верно, {word} — это {meaning}.\n')
            answers[word] = True
        else:
            print(f'Неверно. Правильный ответ {meaning}.\n')
            answers[word] = False

    points = len([key for key in answers.keys()if answers[key]])

    print(f"Вот и всё! Игра закончена. Правильно отвечены слова: "
          f"{', '.join(key for key, value in answers.items() if value)}.")
    print(f"Неправильно отвечены слова: {', '.join(key for key, value in answers.items() if not value)}.")
    print(f"Твой уровень: {levels[points]}.")


if __name__ == "__main__":
    main()
