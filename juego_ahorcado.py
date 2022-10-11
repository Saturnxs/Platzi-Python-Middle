import os, random


def route():
    leaving = False
    
    while not leaving:
        # os.system('cls')
        
        match menu():
            case 1:
                game()
            case 2:
                print('Puntaje')
            case 3:
                leaving = True
                print('Bye bye')
            case other:
                print('Ingresa una opcion valida') 
    
    
def menu():
    option = 0
    
    print("\n¡Bienvenido al juego del ahorcado!\n")
    print("\n1. Nueva partida")
    print("2. Mi puntaje")
    print("3. Salir")

    try:
        option = int(input("\nIngresa una opción: "))
    except ValueError:
        print("Por favor, ingrese un número 🤠")
    
    return option


def sortWord():
    names = []
    with open("./files/data.txt", "r", encoding="utf-8") as file:
        for name in file:
            names.append(name.strip())
            
    return names[random.randint(0, len(names))]

        
def game():
    selectedWord = sortWord()
    hiddenWord = [("_") for letter in selectedWord]
    wordLenght = len(selectedWord)

    moves = 0
    won = False
    
    while wordLenght > 0:
        os.system('cls')
        print("\nNueva partida\n")
        print("\nAdivina la palabra\n")
        print(" ".join(hiddenWord))

        letter = input("\nIngresa una letra: ").lower()
        
        lettersFound = checkLetter(selectedWord, letter)
        if(len(lettersFound) > 0):
            updateHiddenWord(lettersFound, hiddenWord, letter)
            wordLenght = wordLenght - len(lettersFound)
    
    
def checkLetter(word, letter):
    matchingLettersIndex = []
    for index, character in enumerate(word):
        if(character == letter):
            matchingLettersIndex.append(int(index))
    return matchingLettersIndex

    
def updateHiddenWord(lettersFound, hiddenWord, letter):
    for index in lettersFound:
        hiddenWord[index] = letter.upper()
    return hiddenWord
            
        
def run():
    route()  
    

if __name__ == "__main__":
    run()