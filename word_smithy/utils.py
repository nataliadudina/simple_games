import requests
import random

from game_data import BasicWord


def load_random_word():
    """
    Получает список слов с внешнего ресурса.
    Выберет случайное слово.
    Создаст экземпляр класса BasicWord и возвращает его.
    """
    data = requests.get(url='https://jsonkeeper.com/b/7N40', verify=False)
    words_dict = data.json()
    choice_word = random.choice(words_dict)

    basic_word = BasicWord(choice_word['word'], choice_word['subwords'])
    return basic_word
