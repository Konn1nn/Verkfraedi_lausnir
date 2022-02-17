filename = input('Filename: ') # do not change this line

BAD_CHARACTERS = " \n\t"

# Your code here...
f = open(filename, "r")

final_string = ""

for line in f:
    for character in line:
        if character not in BAD_CHARACTERS:
            final_string += character

print(final_string)
