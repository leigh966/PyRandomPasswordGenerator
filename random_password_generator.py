import random
import string
selection = string.ascii_letters + "1234567890!\"£$&"
output = ""
for i in range(0,15):
    output += random.choice(selection)
print(output)
