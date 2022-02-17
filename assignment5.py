input_str = input('Write a word: ') # do not change this line

for i in range(1,len(input_str)):
    print(input_str[:i])

for i,c in enumerate(input_str):
    print(' '*i, end='')
    print(input_str[i:])


