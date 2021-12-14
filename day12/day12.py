def passagePathing(file):

    f = open(file, "r")

    master_lst = []
    for i in f.readlines():
        lines = i.strip().split("-")
        master_lst.append(lines)

    # if there is a capital or if there is a start at the end then the line can be reversed
    for i in master_lst:
        if (i[0].isupper() and not (i[1] == "end")) or (i[1] == 'start'):
            master_lst.append([i[1], i[0]])

    start_lst = []
    # Grab all the start ones
    for i in master_lst:
        if i[0] == 'start':
            start_lst.append(i)

    iter_list = [x for x in master_lst if x not in start_lst]
    iter_list_copy = iter_list.copy()

    combination_lst = []

    for i in start_lst[0:1]:

        print(i)
        # Finding the path using first combination
        curr_lst = i
        combination_lst.append(i)
        condition = True

        while len(curr_lst[1]) < 2 and condition:
            for idx,j in enumerate(iter_list_copy):
                if curr_lst[1] == j[0]:
                    iter_list_copy.pop(idx)
                    combination_lst.append(j)
                    break

                if idx+1 == len(iter_list_copy) and curr_lst[1] != j[0]:
                    condition = False

            curr_lst = j


            print("Current list:", iter_list_copy, "Current element:",curr_lst)

        print(combination_lst)

print(passagePathing("day12/day12_2021_input"))
