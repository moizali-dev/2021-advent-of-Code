#############
### DAY 4 ###
#############
import numpy as np
from io import StringIO

def giant_squid_bingo(file):

    f = open(file, "r")

    rand_number_lst = []
    arr_lst = []
    txt = ""
    for i, j in enumerate(f.readlines()):
        #        print(j.strip())
        # Creating a list for rand_number_lst based on first file line
        if i == 0:
            rand_number = j.strip().split(",")
            for r in rand_number:
                rand_number_lst.append(r)

        else:
            if i % 7 == 0:
                print(txt)
                new_text = StringIO(txt)
                arr = np.loadtxt(new_text, skiprows=1)
                arr_lst.append(arr)
                txt = ""
                txt += j
            else:
                txt += j

    new_text = StringIO(txt)
    arr = np.loadtxt(new_text, skiprows=0)
    arr_lst.append(arr)

    for i in arr_lst:
        print(i)
    f.close()

giant_squid_bingo("day4/day4_2021_input")
