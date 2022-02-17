
def count_case(my_string):
    upper_counter = 0
    lower_counter = 0
    for letter in my_string:
        if letter.isupper():
            upper_counter += 1
        if letter.islower():
            lower_counter += 1
    return upper_counter, lower_counter


if __name__ == "__main__":
    words = ["eR eKkI hÆgT aÐ sLökKvA á ÞeSsU?!", "However, Marie found the best solution"]
    for word in words:
        print("Enter a string: ", word)
        upper_number, lower_number = count_case(word)
        print("Upper case count: ", upper_number)
        print("Lower case count: ", lower_number, end='\n\n')
