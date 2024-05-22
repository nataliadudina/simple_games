import random
answers = ['Absolutely!', 'Chances aren\'t good', 'There is a good chance.', 'The stars say "NO".',
           'Focus and ask again', 'So it shall be!', 'Better don\'t ask.', 'Yes! Wait, no.',
           'Be sure!', 'Doubtfully.', 'The Universe says "Yes"!', 'No doubts!', '404 error...',
           'There is a better way.', 'Don\'t bet on it.', 'You can count on it.', 'Very unlikely.',
           'Heh, heh, heh.', 'Yes, but lately.', 'Chances are 50/50.']


def is_question(text):
    """Граммар-наци"""
    while '?' not in text:
        text = input('Is it a question? Ask again. And do not forget "?".\n')
    if '?' in text:
        return get_random_answer()


def get_random_answer():
    """Получить случайный ответ."""
    print(random.choice(answers))


def ask_question():
    """Получить вопрос и проверить вопрос ли это."""
    while True:
        user_question = input(f'Ask your question.\n')
        is_question(user_question)
        break

def main():
    # основная программа
    print('Hello, World, I am a magic ball, I know all the answers.')
    name = input('What is your name?\n')
    print(f'Hello, {name.capitalize()}!')
    ask_question()

    print()
    while True:
        user_answer = input('One more question? Yep / Nope.\n').lower()
        if user_answer == 'no' or user_answer == 'nay' or user_answer == 'nope':
            print('As you wish. Come back soon!')
            break
        elif user_answer == 'yes' or user_answer == 'yeah' or user_answer == 'yep':
            ask_question()
            print()
        else:
            print('I did not get you. Come again.')


if __name__ == '__main__':
    main()
