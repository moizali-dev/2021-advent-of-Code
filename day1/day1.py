#############
### DAY 1 ###
#############

def larger_than_prev(file):

    f = open(file, "r")

    lst = []
    for i in f.readlines():
        lst.append(int(i.strip()))

    count = 0
    for i in range(1,len(lst)):
        if lst[i] > lst[i-1]:
            count += 1

    return count

def larger_than_prev_sliding_window(file):

    f = open(file, "r")

    lst = []
    for i in f.readlines():
        lst.append(int(i.strip()))

    # sum_lst = []
    # for i in range(0, len(lst)-2):
    #     sum_int = lst[i] + lst[i+1] + lst[i+2]
    #     sum_lst.append(sum_int)

    count = 0
    for i in range(3,len(lst)):
        if lst[i] > lst[i-3]:
            count += 1

    return count

print(larger_than_prev("day1/day1_2021_input"))
print(larger_than_prev_sliding_window("day1/day1_2021_input"))
