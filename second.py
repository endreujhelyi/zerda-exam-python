# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

import os

def letter_counter(file_name, word):
    multiplier = 10
    if not os.path.isfile(file_name):
        return False
    else:
        text = open(file_name, 'w')
        for _ in range(multiplier):
            text.write(word)
        text.close()
        return True
        
