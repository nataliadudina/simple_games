from hangman_utility import display_hangman,  is_invalid, check_input
import random

word_list = ['grumpy', 'miserable', 'gloomy', 'stupefied', 'uptight', 'delighted', 'jittery', 'resentful',
             'overjoyed', 'furious', 'perplexed', 'elated', 'baffled', 'contented', 'startled', 'determined',
             'exuberant', 'aggravated', 'dismayed', 'hesitant', 'apprehensive', 'overwhelmed', 'tranquil',
             'reluctant', 'directionless', 'spiteful', 'thrilled', 'fatigued', 'starving', 'astounded', 'cross',
             'drowsy', 'fearful', 'suspicious', 'outraged', 'weepy', 'stunned', 'indignant', 'weary', 'abashed',
             'listless', 'wistful', 'content', 'assured', 'joyful']

guessed_list = []   # список уже названных слов


def get_word():
    random_word = random.choice(word_list).upper()
    while True:
        if random_word in guessed_list:
            random_word = random.choice(word_list).upper()
        else:
            return random_word


def new_game():
    """Запрос на новый раунд игры"""

    while True:
        user_choice = input('Do you want to play again? Yes / No: ').lower()
        if user_choice == 'no' or user_choice == 'nay' or user_choice == 'nope' or user_choice == 'n':
            print(f'Ok. Today you have guessed {len(guessed_list)} word(s): {", ".join(guessed_list)}.\nCome back any time!')
            break
        elif user_choice == 'yes' or user_choice == 'yeah' or user_choice == 'yep' or user_choice == 'y':
            print()
            play()
            print()
        else:
            print('I did not get you. Come again.')


def play():
    guessed_letters = []  # список уже названных букв
    word = get_word()
    word_completion = ['*'] * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    # guessed_words = []  # список уже названных слов
    tries = 6            # количество попыток

    print(f'Here is your word to guess: {"*" * len(word)}. {len(word)} letters.\nYou have 6 attempts.')
    print(display_hangman(tries))
    # print(word)

    while tries > 0:
        letter = input('Your move: ').upper()
        letter = is_invalid(letter)
        letter = check_input(letter)

        if letter in guessed_letters:
            print('The letter was already named. Enter another letter.')
            print()
        elif letter not in word:
            guessed_letters.append(letter)
            print(f'Ouch! There is no such letter in the hidden word. {tries} attempts left.', *word_completion)
            tries -= 1
            print()
            print(display_hangman(tries))
            print()
        else:
            guessed_letters.append(letter)
            for i in range(len(word)):
                if word[i] == letter:
                    word_completion[i] = letter
            print('Good guess!', *word_completion)
            print()

        if word_completion.count('*') == 0:
            print(f'Congratulations! You have guessed the word {word}.')
            guessed_list.append(word)
            break
        elif tries == 0:
            print(f'Oh, no! There no attempts left...\nThe hidden word was {word}')
            break
    new_game()


# шапка игры
input('Hi there! Let\'s play Hangman! Press Enter to start.')
print('The topic is feelings and emotions.')
play()
