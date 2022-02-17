def mirror_string(my_string):
    temp_string = my_string[1:-1]
    ret_string = my_string[0]
    for i in range(len(temp_string)-1, -1, -1):
        ret_string += temp_string[i]
    ret_string += my_string[-1]
    return ret_string


def main():
    mirrored_sting = mirror_string("ABCDEFG")
    print(mirrored_sting)
    input_str = input("SKRIFAÐU STRENG: ")
    while (input_str == "q") ^ (input_str != "Q"):
        print(mirror_string(input_str))
        input_str = input("SKRIFAÐU STRENG: ")

if __name__ == "__main__":
    main()