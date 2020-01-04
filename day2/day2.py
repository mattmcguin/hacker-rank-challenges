def minimumBribes(q):
    minimum_bribes = 0

    for x, p in enumerate(q):
        # If the person is more than 2 places ahead then it's too chaotic
        if (p - 1) - x > 2:
            print("Too chaotic")
            return

        # Check at most two places in front of where we are and see if bribes took place
        for y in range(max(0, p - 2), x):
            if q[y] > p - 1:
                minimum_bribes += 1

    print(minimum_bribes)


file = open("input.txt", "r")

number_of_test_cases = int(file.readline())

for x in range(number_of_test_cases):
    number_of_people = int(file.readline())
    array = list(map(int, file.readline().rstrip().split()))
    minimumBribes(array)
