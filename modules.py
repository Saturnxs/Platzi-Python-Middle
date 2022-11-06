import sys

# Printing the list of directories that Python searches for modules.
print(sys.path)



import re

text = 'Mi numero de telefono es 1234 1234, el codigo de pais es 506, mi numero de la suerte es el 4'

# Finding all the numbers in the text.
result = re.findall('[0-9]+', text)
print(result) # ['1234', '1234', '506', '4']



import time

# Printing the current time in seconds since the epoch.
timestamp = time.time()
print(timestamp) # 1667769533.4424791

# Printing the current time in a human readable format.
local = time.localtime()
result = time.asctime(local)
print(result) # Sun Nov  6 15:18:53 2022



import collections

numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
# Counting the number of times each number appears in the list.
counter = collections.Counter(numbers)
print(counter) # Counter({1: 4, 2: 2, 3: 2, 4: 1, 5: 1, 21: 1})

