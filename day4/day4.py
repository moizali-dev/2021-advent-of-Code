#############
### DAY 4 ###
#############
import numpy as np
from io import StringIO

def giant_squid_bingo(file):

    f = open(file, "r")

    # Load the rand number in @rand_number_lst and the matrics as an array in @arr_lst
    rand_number_lst = []
    arr_lst = []
    txt = ""
    for i, j in enumerate(f.readlines()):
        #        print(j.strip())
        # Creating a list for rand_number_lst based on first file line
        if i == 0:
            k = i + 6 + 1
            rand_number = j.strip().split(",")
            for r in rand_number:
                rand_number_lst.append(r)

        else:
            if i == k:
                k = i + 6
                new_text = StringIO(txt)
                arr = np.loadtxt(new_text, skiprows=0)
                arr = arr.astype(np.int)
                arr_lst.append(arr)
                txt = ""
                txt += j
            else:
                txt += j

    new_text = StringIO(txt)
    arr = np.loadtxt(new_text, skiprows=0)
    arr = arr.astype(np.int)
    arr_lst.append(arr)

    # Update the arr_lst_update
    def update_arr(arr, i):
        return np.where(arr == i, -1, arr)

    # update the arr_lst
    for i in rand_number_lst:
        lst = []
        for j in arr_lst:
            arr_temp = update_arr(j, int(i))
            lst.append(arr_temp)
        arr_lst = lst.copy()

        # Check if an arr has vertical or diagonal as -1
        for a in arr_lst:
            if -5 in a.sum(axis=0) or -5 in a.sum(axis=1):
                return a[a != -1].sum() * int(i)

print(giant_squid_bingo("day4/day4_2021_input"))

def giant_squid_bingo_part2(file):

    f = open(file, "r")

    # Load the rand number in @rand_number_lst and the matrics as an array in @arr_lst
    rand_number_lst = []
    arr_lst = []
    txt = ""
    for i, j in enumerate(f.readlines()):
        #        print(j.strip())
        # Creating a list for rand_number_lst based on first file line

        if i == 0:
            k = i + 6 + 1
            rand_number = j.strip().split(",")
            for r in rand_number:
                rand_number_lst.append(r)

        else:
            if i == k:
                k = i + 6
                new_text = StringIO(txt)
                arr = np.loadtxt(new_text, skiprows=0)
                arr = arr.astype(np.int)
                arr_lst.append(arr)
                txt = ""
                txt += j
            else:
                txt += j

    new_text = StringIO(txt)
    arr = np.loadtxt(new_text, skiprows=0)
    arr = arr.astype(np.int)
    arr_lst.append(arr)

    # Update the arr_lst_update
    def update_arr(arr, i):
        return np.where(arr == i, -1, arr)

    winner_idx_lst = []
    # update the arr_lst
    for i in rand_number_lst:
        lst = []
        for j in arr_lst:
            arr_temp = update_arr(j, int(i))
            lst.append(arr_temp)
        arr_lst = lst.copy()

        # Check if an arr has vertical or diagonal as -1 and create list with index of winners
        for idx, a in enumerate(arr_lst):
            if -5 in a.sum(axis=0) or -5 in a.sum(axis=1):
                if idx not in winner_idx_lst:
                    winner_idx_lst.append(idx)
                    #print(len(arr_lst), len(winner_idx_lst), i)

                if (len(arr_lst) == len(winner_idx_lst)):
                    a = arr_lst[winner_idx_lst[-1]]
                    return a[a != -1].sum() * int(i)


print(giant_squid_bingo_part2("day4/day4_2021_input"))
