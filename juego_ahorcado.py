import os, random


def menu():
    """
    It's a function that clears the screen, prints a menu, and then depending on the user's input,
    either runs the game, prints the score, or exits the game
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
    It opens a file, reads the contents, and returns a random word from the file
    :return: The word selected
    """
    names = []
    wordSelected = ""
    
    with open("./files/data.txt", "r", encoding="utf-8") as file:
        for name in file:
            names.append(name.strip())
    wordSelected = names[random.randint(0, len(names))]
    
    # Replacing the accented vowels with their non-accented counterparts.
    wordSelected = wordSelected.replace("á", "a")
    wordSelected = wordSelected.replace("é", "e")
    wordSelected = wordSelected.replace("í", "i")
    wordSelected = wordSelected.replace("ó", "o")
    wordSelected = wordSelected.replace("ú", "u")
    
    return wordSelected

        
def game():
    """
    It creates a list of underscores that is the same length as the word that the user is trying to
    guess, and then it asks the user to input a letter. If the letter is in the word, it updates the
    list of underscores. If it isn't, it prints a message
    """
    # Creating a list of underscores that is the same length as the word that the user is trying to guess.
    selectedWord = sortWord()
    hiddenWord = [("_") for letter in selectedWord]
    wordLenght = len(selectedWord)
    
    
    # Creating a list of found letters and a message to be displayed to the user.
    foundLetters = []
    gameMessage = ""
    
    while wordLenght > 0:
        # The game loop. It prints the game board, asks the user to input a letter, and then checks if
        # the letter is in the word. If it is, it updates the hidden word. If it isn't, it prints a
        # message.
        
        os.system('cls')
        print("\n--------- Nueva partida ---------")
        print("\nAdivina la palabra\n")
        print(" ".join(hiddenWord))
        
        print("\n"+gameMessage)
        try:  
            # It's asking the user to input a letter, and then it's checking if the input is a letter.
            # If it isn't, it raises a ValueError.
            letter = input("Ingresa una letra: ").lower()
            if (len(letter) != 1 or letter.isdigit()):
                raise ValueError('Ingresa solamente una letra')
            
            if(letterWasNotFound(foundLetters, letter)):
                foundLetterIndexes = getLettersIndexes(selectedWord, letter)
                if(len(foundLetterIndexes) > 0):
                    wordLenght = wordLenght - len(foundLetterIndexes)
                    updateHiddenWord(foundLetterIndexes, hiddenWord, letter)
                    foundLetters.append(letter)
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

            print("\n█▀▀ ▄▀█ █▄░█ ▄▀█ █▀ ▀█▀ █▀▀\n█▄█ █▀█ █░▀█ █▀█ ▄█ ░█░ ██▄\n")
            print("La palabra era  "+" ".join(hiddenWord)+"\n")
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
        if(character == letter):
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
        if(letter == newLetter):
            return False
    return True

        
def run():
    menu()  
    

if __name__ == "__main__":
    run()