# Hangman

def get_string():
    temp_string = input()
    temp_string.upper()
    return temp_string

def check_guess(guess_word, letter_string) -> bool:
    length_of_word = len(guess_word)
    guess_word_unique = set(guess_word)
    unique_count = len(guess_word_unique)
    guess_list = ["W"] * length_of_word
    letter_string = letter_string[:(10+unique_count)]
    for guess in letter_string:
        for index, letter in enumerate(guess_word):
            if letter == guess:
                guess_list[index] = "R"
    if "W" not in guess_list:
        return True
    else:
        return False

def did_win(my_bool):
    if my_bool:
        print("WIN")
    else:
        print("LOSE")

def main():
    guess_word = get_string()
    letter_string = get_string()
    win_loose = check_guess(guess_word, letter_string)
    did_win(win_loose)


if __name__ == "__main__":
    main()
""" 
Test cases:
HANGMAN
ABCDEFGHIJKLMNOPQRSTUVWXYZ

BANANA
ABCDEFGHIJKLMNOPQRSTUVWXYZ

RAINBOWS
USIANBVLOJRKWXZCTQGHPFMYDE
"""