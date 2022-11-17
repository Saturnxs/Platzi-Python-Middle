def openFile():
    file = open("./files/names.txt")
    print(file.read()) # Leer todo como lista
    # Fancundo
    # Miguel
    # Pablo
    # Pepe
    # LolÃ³
    # Hector
    # Lisa
    # Maria
    
    
    # Leer linea a linea
    print(file.readline()) # Fancundo
    print(file.readline()) # Miguel
    print(file.readline()) # Pablo
    
    file.close() # Cerrar el archivo libera memoria de Python
    
    # Malas prácticas, es mejor usar el with open
    

def readNumbers():
    """
    It opens the file, reads each line, converts it to an integer, and adds it to a list
    """
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            numbers.append(int(line));
    print(numbers)
    # [13, 2453, 334, 53, 753, 4, 3535, 52, 424623, 4634, 3, 244, 43566, 3453, 34334]


def write():
    """
    It opens a file called "names.txt" in the "files" directory, and writes the names in the "names"
    list to it
    """
    names = ["Fancundo","Miguel","Pablo","Pepe","Loló","Hector",]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    
    names = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as names:
        for line in names:
            names.append(line);
    print(names) # ["Fancundo","Miguel","Pablo","Pepe","Loló","Hector",]
           
            
def append():
    """
    It opens the file in append mode, then loops through the list of names and writes each name to the
    file, followed by a newline character
    """
    names = ["Lisa","Maria"]
    with open("./files/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    
    result = []
    with open("./files/names.txt", "r", encoding="utf-8") as names:
        for line in names:
            result.append(line);
    print(result)
    # ['Fancundo\n', 'Miguel\n', 'Pablo\n', 'Pepe\n', 'Loló\n', 'Hector\n', 'Lisa\n', 'Maria\n']
    
          
            
def readNames():
    """
    It opens the file, reads each line, strips the line of any whitespace, and adds it to a list
    """
    names = []
    with open("./files/names.txt", "r", encoding="utf-8") as f:
        for name in f:
            if len(name.strip()) > 0:
                names.append(name.strip())
            else:
                print("Archivo vacio")
        print(names)


if __name__ == "__main__":
    append()