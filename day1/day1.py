def rotate_array_left(a, d):
    rotated_array = list(a)
    for x in range(len(a)):
        rotated_array[x - d] = a[x]
    return rotated_array


file = open("input.txt", "r")

size_of_array = int(file.readline())
number_of_left_rotations = int(file.readline())
array = list(map(int, file.readline().rstrip().split()))

print(rotate_array_left(array, number_of_left_rotations))
