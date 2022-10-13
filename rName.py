#18238

import random

x = random.randint(0, 18238)

file = open("names.txt", "r")
content = file.readlines()
print(content[x])