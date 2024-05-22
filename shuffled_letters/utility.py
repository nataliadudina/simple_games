import random


def load_words(filename):
    """Читает текстовый файл. Возвращает список из 5 случайных слов."""

    with open(filename, encoding='utf-8') as file:
        words_list = [w.strip() for w in file.readlines()]
        random.shuffle(words_list)
        return words_list[:5]


def get_word(word):
    """Получает слово. Меняет местами буквы. Возвращает строку букв"""

    word = list(word)
    random.shuffle(word)
    return ' '.join(word)


def record_history(filename, name, score):
    """Принимает имя и очки игрока, записывает их в текстовый файл"""

    with open(filename, 'a', encoding='utf-8') as input:
        print(f'{name}: {score}', file=input)


def get_history(filename):
    """Читает текстовый файл, возвращает количество игр и лучший результат"""

    with open(filename, encoding='utf-8') as output:

        top_scores = 0
        games = 0
        for line in output.readlines():
            games += 1
            scores = int(line.split(':')[1])
            if scores > top_scores:
                top_scores = scores

        return games, top_scores
