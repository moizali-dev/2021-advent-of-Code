import numpy as np
from tqdm import tqdm

def lanternfish(file):

    # Adding to numpy array from file
    f = open(file, "r")

    for i in f.readlines():
        n = i.split(",")

    A = np.array([])
    for j in n:
        A = np.append(A, int(j))

    # print(A)
    # Creating simulation for 80 days
    for i in tqdm(range(256)):

        # Condition if there are zeros
        number_of_zeros = (A == 0).sum()
        if number_of_zeros > 0:
            for i in range(number_of_zeros):
                A = np.append(A, 9)

        A = np.where(A == 0, 7, A)

        # Subtracting one for each day
        A = A - 1
        # print(A)

    print(A.size)



def lanternfishpart2(file):

    # Adding to numpy array from file
    f = open(file, "r")

    for i in f.readlines():
        n = i.split(",")

    fishes = []
    for j in n:
        fishes.append(int(j))

    days = [0] * 9
    # Update the current numbers
    print(fishes)
    for fish in fishes:
        days[fish] += 1
        print(days)
    for i in range(256):
        # To make it cyclic: 0, 1, 2, 3, 4, 5, 6, 7, 8
        today = i % len(days)    # Add new babies

        print(today, days)
        days[(today + 7) % len(days)] += days[today]

    print(f'Total lanternfish after 256 days: {sum(days)}')

lanternfish("day6/day6_2021_input")
lanternfishpart2("day6/day6_2021_input")