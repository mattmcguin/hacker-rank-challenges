def minimumSwaps(arr):
    ref_arr = sorted(arr)
    index_dict = {v: i for i, v in enumerate(arr)}
    swaps_needed = 0

    for index, value in enumerate(arr):
        correct_value = ref_arr[index]
        if value != correct_value:
            to_swap_index = index_dict[correct_value]
            arr[to_swap_index] = arr[index]
            arr[index] = arr[to_swap_index]
            index_dict[value] = to_swap_index
            index_dict[correct_value] = index
            swaps_needed += 1

    return swaps_needed


file = open("input.txt", "r")

size_of_array = int(file.readline())
array = list(map(int, file.readline().rstrip().split()))

print(minimumSwaps(array))
