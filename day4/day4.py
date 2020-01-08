def arrayManipulation(n, queries):

    manipulated_array = [0] * (n + 1)

    for arr in queries:
        beginning = arr[0]
        end = arr[1]
        total = arr[2]
        manipulated_array[beginning - 1] += total
        if (end) <= n:
            manipulated_array[end] -= total

    max_amount = 0
    temp_max = 0
    for x in range(n):
        temp_max += manipulated_array[x]
        if max_amount < temp_max:
            max_amount = temp_max

    return max_amount


file = open("input.txt", "r")

first_line = file.readline().split()

array_size = int(first_line[0])
number_of_test_cases = int(first_line[1])

queries = []

for x in range(number_of_test_cases):
    array = list(map(int, file.readline().rstrip().split()))
    queries.append(array)


print(arrayManipulation(array_size, queries))
