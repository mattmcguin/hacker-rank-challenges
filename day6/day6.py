def twoStrings(s1, s2):
    for letter in s2:
        if letter in s1:
            return "YES"

    return "NO"


file = open("input.txt", "r")

number_of_test_cases = int(file.readline())

for x in range(number_of_test_cases):
    first_word = file.readline()
    second_word = file.readline()
    print(twoStrings(first_word, second_word))

