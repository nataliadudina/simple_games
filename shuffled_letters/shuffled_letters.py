from utility import load_words, get_word, record_history, get_history


def new_game():
    """Запрос на новый раунд игры"""

    while True:
        user_choice = input('Wanna play again? Yes / No: ').lower()
        if user_choice == 'no' or user_choice == 'nay' or user_choice == 'nope' or user_choice == 'n':
            print('As you wish. Come back soon!')
            break
        elif user_choice == 'yes' or user_choice == 'yeah' or user_choice == 'yep' or user_choice == 'y':
            print()
            game()
            print()
        else:
            print('I did not get you. Come again.')


def game():
    """
    Запрашивает 5 слов с перемешанными буквами, выводит их по одному.
    Ведётся счёт.
    """

    scores = 0
    words_list = load_words('words.txt')

    for word in words_list:
        word_to_guess = get_word(word)
        print(f'Guess the word: {word_to_guess}')
        player_answer = input('Your answer: ')
        if player_answer.lower().strip() == word:
            scores += 10
            print(f'Right answer! It is {word}. You get 10 scores!')
            print()
        else:
            print(f'Wrong answer! It is {word}.')
            print()

    record_history('history.txt', player_name, scores)
    games, top_scores = get_history('history.txt')

    print(f'That is all. You got {scores}.')
    print(f'Games played: {games}, top scores: {top_scores}')
    new_game()


# шапка игры
player_name = input('Hello! What is your name? \n').capitalize()
print(f"Hello, {player_name}. You need to guess 5 english words. Let's play!")

if __name__ == '__main__':
    game()
