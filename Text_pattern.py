
def add_one_letter(my_string):
    print_string = ""
    for letter in my_string:
        print_string += letter
        print(print_string)
    for i in range(1, len(print_string)):
        print(" " * i, end="")
        print(print_string[i:])


def main():
    add_one_letter("Seathor")

if __name__ == "__main__":
    main()