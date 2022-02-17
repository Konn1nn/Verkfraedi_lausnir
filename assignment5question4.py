

def open_file(file_name):
    f = open(file_name, "r")
    return f

def find_min_max(file):
    max = None
    min = None
    sum_of_numbers = 0
    counter = 0
    for line in file:
        counter += 1
        number = float(line)
        sum_of_numbers += number
        if max == None and min == None:
            max = min = number
        if number > max:
            max = number
        if number < min:
            min = number
    average = sum_of_numbers/counter
    return min, max, average


if __name__ == "__main__":
    try:
        input_str = input("Enter filename: ")
        my_file = open_file(input_str)
        min,max,average = find_min_max(my_file)
        print(f"Min: {min}")
        print(f"Max: {max}")
        print(f"Average: {average}")
    except(FileNotFoundError):
        print("File not found")
    except(FileExistsError):
        print("No file exists")