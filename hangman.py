import random

def start_game():
    word = make_word()
    make_game(word)  # loop

def make_word():
    with open("nouns.txt") as file:
        words = file.readlines()  # 40845 words
        return words[random.randint(0, len(words) - 1)]

def make_game(word):
    hidden_word = ['_'] * (len(word) - 1)
    mistakes = 0
    mistake_list = []
    print(f"Слово: {' '.join(hidden_word)}")

    while mistakes < 9 and '_' in hidden_word:
        user_letter = make_user_input(hidden_word, mistake_list)

        if user_letter in word:
            hidden_word = open_letter_in_mask(word, hidden_word, user_letter)
        else:
            mistake_list.append(user_letter)
            mistakes += 1

        print_res(hidden_word, mistakes, mistake_list)

    if mistakes == 9:
        print_res(hidden_word, mistakes, mistake_list)
        print(f"Загаданное слово: {word}")
        print('Поражение')
    elif not ('_' in hidden_word):
        print(f"Слово: {''.join(hidden_word)}")
        print('Победа')

def make_user_input(hidden_word, mistake_list):
    while True:
        user_letter = input('Введите букву: ').strip().lower()
        if user_letter == "_":
            print("Введите букву кириллического алфавита.")
            continue
        if user_letter.upper() in hidden_word:
            print("Вы уже вводили эту букву.")
            continue
        if user_letter in mistake_list:
            print("Вы уже вводили эту букву.")
            continue
        if not (len(user_letter) == 1):
            print("Введите одну букву.")
            continue
        code = ord(user_letter)
        if code < 1072 or code > 1105:
            print("Введите букву кириллического алфавита.")
            continue
        else:
            print()
            return user_letter


def open_letter_in_mask(word, hidden_word, user_letter):
    letter_index = word.find(user_letter)
    while letter_index >= 0:
        hidden_word[letter_index] = user_letter.upper()
        letter_index = word.find(user_letter, letter_index + 1)
    return hidden_word

def print_res(hidden_word, mistakes, mistake_list):
    word = "Слово: " + ' '.join(hidden_word)
    mist = "Ошибки (" + str(mistakes) + "):" + ', '.join(mistake_list)

    hangman_states = [
        [  # 0
            "       |\n"
            "       |  {}\n"
            "       |\n"
            "       |\n"
            "       |\n"
            "       |\n"
            "========="
        ],
        [  # 1
            "        |\n"
            "        |  {}\n"
            "        |\n"
            "        |  {}\n"
            "___     |\n"
            "========="
        ],
        [  # 2
            "        |\n"
            " |      |  {}\n"
            " |      |\n"
            " |      |  {}\n"
            "_|_     |\n"
            "========="
        ],
        [  # 3
            "  ____  |\n"
            " |      |  {}\n"
            " |      |\n"
            " |      |  {}\n"
            "_|_     |  \n"
            "========="
        ],
        [  # 4
            "  ____  |\n"
            " |   |  |  {}\n"
            " |   O  |\n"
            " |      |  {}\n"
            "_|_     |  \n"
            "========="
        ],
        [  # 5
            "  ____  |\n"
            " |   |  |  {}\n"
            " |   O  |\n"
            " |   |  |  {}\n"
            "_|_     |  \n"
            "========="
        ],
        [  # 6
            "  ____  |\n"
            " |   |  |  {}\n"
            " |   O  |\n"
            " |  /|  |  {}\n"
            "_|_     |  \n"
            "========="
        ],
        [  # 7
            "  ____  |\n"
            " |   |  |  {}\n"
            " |   O  |\n"
            " |  /|\\ | {}\n"
            "_|_     |\n"
            "========="
        ],
        [  # 8
            "  ____  |\n"
            " |   |  |  {}\n"
            " |   O  |\n"
            " |  /|\\ | {}\n"
            "_|_ /   |\n"
            "========="
        ],
        [  # 9
            "  ____  |\n"
            " |   |  |  {}\n"
            " |   O  |\n"
            " |  /|\\ |  {}\n"
            "_|_ / \\ |  \n"
            "========="
        ]
    ]
    formatted_states = [el[0].format(word, mist) for el in hangman_states]
    print(formatted_states[mistakes])


if __name__ == '__main__':
    while True:
        status = input('Начать новую игру или выйти? \nВведите н/в: ')
        if status == 'в':
            exit('До новых встреч')
        else:
            print('В И С Е Л И Ц А')
            start_game()
