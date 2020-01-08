import collections


def check_magazine(magazine, note):
    try:
        for word in note:
            magazine.remove(word)
        print("Yes")
    except ValueError:
        print("No")


def check_magazine_counter_version(magazine, note):
    if collections.Counter(note) - collections.Counter(magazine) == {}:
        print("Yes")
    else:
        print("No")


file = open("input.txt", "r")

first_line = file.readline().split()

magazine_size = int(first_line[0])
note_size = int(first_line[1])

magazine = list(map(str, file.readline().rstrip().split()))
note = list(map(str, file.readline().rstrip().split()))

check_magazine_counter_version(magazine, note)
