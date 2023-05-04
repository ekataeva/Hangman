import random

def startGame():
    word = makeWord()
    makeGame(word)  # loop

def makeWord():
    word = None
    with open("nouns.txt") as file:
        words = file.readlines()  # 40845 words
        word = words[random.randint(0, len(words) - 1)]
    return  word

def makeGame(word):
    hiddenWord = ['_'] * (len(word) - 1)
    mistakes = 0
    mistakeList = []

    while mistakes < 9 and '_' in hiddenWord:
        userLetter = makeUserInput(hiddenWord, mistakeList)
        hiddenWord, mistakes, mistakeList = checkUserInput(word, hiddenWord, userLetter, mistakes, mistakeList)
        printRes(hiddenWord, mistakes, mistakeList)

    if mistakes == 9:
        print(
            f"  ____ |\n |   | |Слово:  {' '.join(hiddenWord)}\n |   O |\n |  /|\\|Ошибки ({mistakes}): {', '.join(mistakeList)}\n_|_ / \\|  ")
        print(f"Загаданное слово: {word}")
        print('Поражение')
    elif not ('_' in hiddenWord):
        print(f"Слово: {''.join(hiddenWord)}")
        print('Победа')
    else:
        print('Что-то пошло не так...')

def makeUserInput(hiddenWord, mistakeList):
    userLetter = input('Введите букву: ').strip().lower()

    while userLetter.upper() in hiddenWord or userLetter in mistakeList or not (len(userLetter) == 1):
        userLetter = input('Попробуйте снова: ').strip().lower()

    print()
    return userLetter

def checkUserInput(word, hiddenWord, userLetter, mistakes, mistakeList):
    if userLetter in word:
        letterIndex = word.find(userLetter)
        while letterIndex >= 0:
            hiddenWord[letterIndex] = userLetter.upper()
            letterIndex = word.find(userLetter, letterIndex + 1)
    else:
        mistakeList.append(userLetter)
        mistakes += 1

    return hiddenWord, mistakes, mistakeList

def printRes(hiddenWord, mistakes, mistakeList):
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

if __name__ == '__main__':
    while True:
        status = input('Начать новую игру или выйти? \nВведите н/в: ')
        if status == 'в':
            exit('До новых встреч')
        else:
            print('В И С Е Л И Ц А')
            startGame()
