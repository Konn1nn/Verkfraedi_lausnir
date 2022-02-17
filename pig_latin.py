
VOWELS = ("a", "i", "e", "o", "u")

def pig_latin(someword):
    if someword[0] in VOWELS:
        return someword + "yay"
    for letter in someword:
        if letter in VOWELS:
            word_list = someword.split(letter, 1)
            return letter + word_list[1] + word_list[0] + "ay"

if __name__ == '__main__':
    print(pig_latin('PyCharm'))
    words = ["dog", "scratch", "is", "apple", "home"]
    for word in words:
        print("Write a word: ", word)
        print(pig_latin(word))
        print()