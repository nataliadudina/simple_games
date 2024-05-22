class BasicWord:

    def __init__(self, original_word, subwords_set):
        self.original_word = original_word
        self.subwords_set = subwords_set

    def __repr__(self):
        return self.original_word

    def check_word(self, word) -> bool:
        """Проверяет введенное слова в списке допустимых подслов"""
        return word in self.subwords_set

    def count_subwords(self) -> int:
        """Возвращает количество подслов"""
        return len(self.subwords_set)


class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return f'{self.name.capitalize()}'

    def get_used_words_total(self) -> int:
        """Возвращает количество использованных слов """
        return len(self.used_words)

    def add_to_used_words(self, word):
        """Добавляет слова в использованные слова"""
        self.used_words.append(word)

    def is_used(self, word) -> bool:
        """Проверяет слово на использование ранее"""
        return word in self.used_words
