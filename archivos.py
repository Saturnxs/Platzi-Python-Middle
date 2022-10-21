def readNumbers():
    """
    It opens the file, reads each line, converts it to an integer, and adds it to a list
    """
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line));
    print(numbers)


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


def run():
    readNames()


if __name__ == "__main__":
    run()

