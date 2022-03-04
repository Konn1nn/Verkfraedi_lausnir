# Missing numbers

def get_no_cycles():
    number_of_cycles = int(input())
    return number_of_cycles

def get_number_list(number_of_cycles):
    input_list = []
    for i in range(number_of_cycles):
        temp_number = int(input())
        input_list.append(temp_number)
    return input_list

def print_missing_numbers(input_list):
    highest_number = max(input_list)
    missed_number = False
    for i in range(1,highest_number+1):
        if i not in input_list:
            missed_number = True
            print(i)

    if not missed_number:
        print("Good Job!! :D")

def main():
    number_of_cycles = get_no_cycles()
    input_list = get_number_list(number_of_cycles)
    print_missing_numbers(input_list)

if __name__ == "__main__":
    main()