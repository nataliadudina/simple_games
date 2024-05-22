from utils import load_random_word
from game_data import Player


game_word = load_random_word()


def get_unguessed_words(subwords, guessed_words) -> str:
    unguessed_words = set(subwords) - set(guessed_words)
    if len(unguessed_words) == 0:
        return "0"
    return ', '.join(list(unguessed_words))


def main():
    player_name = input('Ввведите имя игрока.\n')
    player = Player(player_name)
    print(f'Привет, {player}! \n'
          f'Составьте {len(game_word.subwords_set)} слов из слова {game_word.original_word.upper()}.\n'
          f'Слова должны быть не короче 3 букв. \n'
          f'Чтобы закончить игру, угадайте все слова или напишите "stop". \n'
          f'Поехали!')

    while len(game_word.subwords_set) != len(player.used_words):
        user_answer = input('Ваше слово: ').lower()
        if user_answer in ('stop', 'стоп'):
            break
        elif len(user_answer) < 3:
            print('Это слишком короткое слово.')
        elif not game_word.check_word(user_answer):
            print('Это неверное слово.')
        elif user_answer in player.used_words:
            print('Это слово уже использовано.')
        else:
            player.used_words.append(user_answer)
            print(f'Хорошее слово. Верно! '
                  f'\nКоличество угаданных слов - {len(player.used_words)} из {len(game_word.subwords_set)}.')
    print(f'Игра завершена. Количество угаданных слов - {len(player.used_words)}!\n'
          f'Неугаданные слова: {get_unguessed_words(game_word.subwords_set, player.used_words)}.')


if __name__ == '__main__':
    main()
