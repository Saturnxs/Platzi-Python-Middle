def readNumbers():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line));
    print(numbers)


def write():
    names = ["Fancundo","Miguel","Pablo","Pepe","Loló","Hector",]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
           
            
def append():
    names = ["Lisa","Maria"]
    with open("./files/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
            
            
def readNames():
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

