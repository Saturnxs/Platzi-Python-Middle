import os, random

# Have to create points system


def menu():
    """
    It's a function that displays a menu, and depending on the option chosen, it either starts a new
    game, displays the score, or exits the program
    """
    leaving = False
    errorMessage = ""
    option = 0

    while not leaving:
        os.system('cls')

        print("\n▄▀█ █░█ █▀█ █▀█ █▀▀ ▄▀█ █▀▄ █▀█\n█▀█ █▀█ █▄█ █▀▄ █▄▄ █▀█ █▄▀ █▄█\n")
        print("1. Nueva partida")
        print("2. Mi puntaje")
        print("3. Salir")

        print("\n"+errorMessage)
        try:
            option = int(input("Ingresa una opción: "))
            match option:
                case 1:
                    game()
                case 2:
                    print('Puntaje')
                case 3:
                    leaving = True
                    os.system('cls')
                    print('¡Gracias por jugar al juego del ahorcado!')
                case other:
                    errorMessage = "Por favor, ingresa una opción válida"
        except ValueError:
            errorMessage = "Por favor, ingresa una opción válida"


def sortWord():
    """
    It's opening a file, reading the contents of the file, and then selecting a random word from the
    file
    :return: the wordSelected variable.
    """
    names = []
    wordSelected = ""
    toNormalize = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"))

    # It's opening a file, reading the contents of the file, and then selecting a random word from the
    # file.
    with open("./files/data.txt", "r", encoding="utf-8") as file:
        for name in file:
            names.append(name.strip())
    wordSelected = names[random.randint(0, len(names))]

    # It's replacing the accented vowels with their non-accented counterparts.
    for accentedLetter, nonAccentedLetter in toNormalize:
        wordSelected = wordSelected.replace(accentedLetter, nonAccentedLetter)
    return wordSelected


def game():  # Calculate difficulty based on word length
    hangmanImages = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="
    ]
    failedChances = 0
    lost = False
    
    # Creating a list of underscores that is the same length as the word that the user is trying to guess.
    selectedWord = sortWord()
    hiddenWord = [("_") for letter in selectedWord]

    wordsNotFound = len(selectedWord)
    foundLetters = []
    gameMessage = ""


    # It's a loop that is running while the user hasn't lost and there are still letters to be found.
    while wordsNotFound > 0 and not lost:
        os.system('cls')
        print("\n▄▀█ █▀▄ █ █░█ █ █▄░█ ▄▀█   █░░ ▄▀█   █▀█ ▄▀█ █░░ ▄▀█ █▄▄ █▀█ ▄▀█\n█▀█ █▄▀ █ ▀▄▀ █ █░▀█ █▀█   █▄▄ █▀█   █▀▀ █▀█ █▄▄ █▀█ █▄█ █▀▄ █▀█\n")
        print(hangmanImages[failedChances])
        print("\n"+" ".join(hiddenWord))

        print("\n"+gameMessage)
        try:
            # It's asking the user to input a letter, and then it's checking if the input is a letter.
            # If it isn't, it raises a ValueError.
            letter = input("Ingresa una letra: ").lower()
            if (len(letter) != 1 or letter.isdigit()):
                raise ValueError('Ingresa solamente una letra')

            # It's checking if the letter that the user guessed is not in the list of found letters. If it isn't,
            # it's checking if the letter is in the word. If it is, it's updating the hidden word, and
            # adding the letter to the list of found letters. If it isn't, it's adding one to the failed chances, and checking
            # if the user has lost.
            if (letterWasNotFound(foundLetters, letter)):
                foundLetterIndexes = getLettersIndexes(selectedWord, letter)
                if (len(foundLetterIndexes) > 0):
                    wordsNotFound = wordsNotFound - len(foundLetterIndexes)
                    updateHiddenWord(foundLetterIndexes, hiddenWord, letter)
                    foundLetters.append(letter)
                else:
                    failedChances = failedChances + 1
                    lost = False if failedChances < 6 else True

                gameMessage = ""
            else:
                gameMessage = "Ya encontraste esta letra"
        except ValueError as ve:
            gameMessage = str(ve)

    else:
        # A loop that asks the user if they want to play again or go back to the menu.
        alertMessage = ""
        option = 0

        while True:
            os.system('cls')
            updateHiddenWord(foundLetterIndexes, hiddenWord, letter)

            print("\n█▀▀ ▄▀█ █▄░█ ▄▀█ █▀ ▀█▀ █▀▀\n█▄█ █▀█ █░▀█ █▀█ ▄█ ░█░ ██▄\n") if not lost else print("\n█▀█ █▀▀ █▀█ █▀▄ █ █▀ ▀█▀ █▀▀\n█▀▀ ██▄ █▀▄ █▄▀ █ ▄█ ░█░ ██▄\n")
            print(hangmanImages[failedChances])
            print("\nLa palabra era  "+" ".join(hiddenWord)+"\n") if not lost else print("\nLa palabra era  "+" ".join(selectedWord).upper()+"\n")
            print("1. Jugar de nuevo")
            print("2. Ir al menu")

            print("\n"+alertMessage)
            try:
                option = int(input("Ingresa una opción: "))
            except ValueError:
                alertMessage = "Por favor, ingresa una opción válida"

            match option:
                case 1:
                    game()
                case 2:
                    break


def getLettersIndexes(word, letter):
    """
    It takes a word and a letter as input, and returns a list of indexes where the letter is found in
    the word

    :param word: The word that the user is trying to guess
    :param letter: The letter that the user guessed
    :return: A list of indexes where the letter is found in the word.
    """
    matchingLettersIndex = []
    for index, character in enumerate(word):
        if (character == letter):
            matchingLettersIndex.append(int(index))
    return matchingLettersIndex


def updateHiddenWord(foundLetterIndexes, hiddenWord, letter):
    """
    It takes a list of indexes, a list of letters, and a letter, and returns a list of letters with the
    letter at the indexes replaced by the letter

    :param foundLetterIndexes: a list of indexes where the letter was found in the word
    :param hiddenWord: The word that the user is trying to guess
    :param letter: The letter that the user guessed
    :return: The hidden word with the letter in the correct position.
    """
    for index in foundLetterIndexes:
        hiddenWord[index] = letter.upper()
    return hiddenWord


def letterWasNotFound(foundLetters, newLetter):
    """
    If the new letter is not in the list of found letters, return True. Otherwise, return False

    :param foundLetters: A list of letters that have been found so far
    :param newLetter: The letter that the user guessed
    :return: a boolean value.
    """
    for letter in foundLetters:
        if (letter == newLetter):
            return False
    return True


def run():
    menu()


if __name__ == "__main__":
    run()