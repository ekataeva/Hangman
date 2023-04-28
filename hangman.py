import random

while True:
    status = input('начать новую игру (_нажмите enter_) или выйти из приложения (_введите "в"_)? ')
    if status == 'в':
        exit(0)
        break
    print('В И С Е Л И Ц А')

    # При начале новой игры, случайным образом загадывается слово
    word = None
    with open("nouns.txt") as file:
        words = file.readlines()  # 40845 words
        word = words[random.randint(0,len(words) - 1)]
    countRightLetters = len(set(word[0:len(word) - 1]))
    hiddenWord = ['_'] * (len(word) - 1)
    guesedLetters = 0
    guesedLettersList = []
    mistakes = 0
    mistakeList = []
    print()

    # игрок начинает процесс отгадывания
    while mistakes < 9 and guesedLetters < countRightLetters:

        userLetter = input('Введите букву: ').strip().lower()
        while userLetter in guesedLettersList or userLetter in mistakeList or not(len(userLetter)  == 1):
            userLetter = input('Вы уже вводили эту букву. Введите другую букву: ').strip().lower()
        print()

        if userLetter in word:
            guesedLettersList.append(userLetter)
            guesedLetters += 1
            letterIndex = word.find(userLetter)
            while letterIndex >= 0:
                hiddenWord[letterIndex] = userLetter.upper()
                letterIndex = word.find(userLetter, letterIndex + 1)
        else:
            mistakeList.append(userLetter)
            mistakes += 1

        match mistakes:
            case 8:
                print(
                    f"  ____ |\n |   | |  Слово:  {' '.join(hiddenWord)}\n |   O |\n |  /|\\| Ошибки ({mistakes}): {', '.join(mistakeList)}\n_|_ /  |  ")
            case 7:
                print(
                    f"  ____ |\n |   | |  Слово:  {' '.join(hiddenWord)}\n |   O |\n |  /|\\| Ошибки ({mistakes}): {', '.join(mistakeList)}\n_|_    |  ")
            case 6:
                print(
                    f"  ____ |\n |   | |  Слово:  {' '.join(hiddenWord)}\n |   O |\n |  /| |  Ошибки ({mistakes}): {', '.join(mistakeList)}\n_|_    |  ")
            case 5:
                print(
                    f"  ____ |\n |   | |  Слово:  {' '.join(hiddenWord)}\n |   O |\n |   | |  Ошибки ({mistakes}): {', '.join(mistakeList)}\n_|_    |  ")
            case 4:
                print(
                    f"  ____ |\n |   | |  Слово:  {' '.join(hiddenWord)}\n |   O |\n |     |  Ошибки ({mistakes}): {', '.join(mistakeList)}\n_|_    |  ")
            case 3:
                print(
                    f"  ____ |\n |     |  Слово:  {' '.join(hiddenWord)}\n |     |\n |     |  Ошибки ({mistakes}): {', '.join(mistakeList)}\n_|_    |  ")
            case 2:
                print(
                    f"       |\n |     |  Слово:  {' '.join(hiddenWord)}\n |     |\n |     |  Ошибки ({mistakes}): {', '.join(mistakeList)}\n_|_    |  ")
            case 1:
                print(
                    f"       |\n       |  Слово:  {' '.join(hiddenWord)}\n       |\n       |  Ошибки ({mistakes}): {', '.join(mistakeList)}\n___    |  ")
            case 0:
                print(
                    f"       |\n       |  Слово:  {' '.join(hiddenWord)}\n       |\n       |  \n       |  ")

        print()

    if mistakes == 9:
        print(f"  ____ |\n |   | |Слово:  {' '.join(hiddenWord)}\n |   O |\n |  /|\\|Ошибки ({mistakes}): {', '.join(mistakeList)}\n_|_ / \\|  ")
        print(f"Загаданное слово: {word}")
        print('Вы проиграли!')
    elif guesedLetters == countRightLetters:
        print(f"Слово: {''.join(hiddenWord)}")
        print('Вы выиграли!')
    else:
        print('Что-то пошло не так...')

    print()





