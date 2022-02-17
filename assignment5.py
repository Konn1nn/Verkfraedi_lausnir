
filename = input('Filename: ') # do not change this line

# your code here

def open_file(file_name):
    f = open(file_name, "r")
    return f

def average_numbers(file):
    sum_file = 0
    counter = 0
    for line in file:
        sum_file += int(line)
        counter += 1
    sum_file = sum_file/counter
    return sum_file


if __name__ == "__main__":
    my_file = open_file(filename)
    my_sum = average_numbers(my_file)
    print(my_sum)