import numpy as np

def Seven_Segment_Search(file, part2 = False):

    lines = np.genfromtxt(file, delimiter=" | ", dtype='str')

    ## Part 1 ###
    count = 0
    for i in range(len(lines)):
        split_lines = (lines[i][1].split(" "))
        for j in split_lines:
            if len(j) in [2,4,3,7]: # 1,4,7,8
                count += 1

    print(f'Solution for part 1: {count}')

    ### Part 2 ###

    '''
    # Condition to check between 0, 6 and 9: If len is 6 and contains all letters from number 4, then it is 9,
    # else if contains difference of 4 and 7 then 6
    # else its 0
    
    # Condition to check between 2, 3 and 5 : if len is 5 and intersect is 4 and if letters in 1 then 3 else 2
    # Remining number is 5:
    '''

    total_number = 0

    for i in range(len(lines)):
        input_code, output_code = lines[i][0].split(" "), lines[i][1].split(" ")

        # print( input_code, output_code)
        # Create a dictionary to save the encrypted letters as keys and values as their numbers
        dic = {}
        idx_to_rem = []
        for idx, j in enumerate(input_code):
            if len(j) == 2:
                x = "".join(sorted(j))
                dic[x] = 1
                idx_to_rem.append(idx)
            elif len(j) == 4:
                x = "".join(sorted(j))
                dic[x] = 4
                idx_to_rem.append(idx)
            elif len(j) == 3:
                x = "".join(sorted(j))
                dic[x] = 7
                idx_to_rem.append(idx)
            elif len(j) == 7:
                x = "".join(sorted(j))
                dic[x] = 8
                idx_to_rem.append(idx)

        idx_to_rem = sorted(idx_to_rem)
        # print(idx_to_rem, input_code)

        updated_input_code = []
        for i in range(len(input_code)):
            if i not in idx_to_rem:
                updated_input_code.append(input_code[i])

        # print(dic)

        key_for_1 = list(dic.keys())[list(dic.values()).index(1)]
        key_for_4 = list(dic.keys())[list(dic.values()).index(4)]
        diff_1_4 = list(set(key_for_1).symmetric_difference(set(key_for_4)))

        # Checkcing for number 9
        for idx, j in enumerate(updated_input_code):
            if len(j) == 6 and key_for_4[0] in j and key_for_4[1] in j and key_for_4[2] in j and key_for_4[3] in j:
                x = "".join(sorted(j))
                dic[x] = 9
                idx_to_rem2 = idx

        del updated_input_code[idx_to_rem2]

        # print(dic)

        # Checking for number 6
        key_for_9 = list(dic.keys())[list(dic.values()).index(9)]
        key_for_8 = list(dic.keys())[list(dic.values()).index(8)]
        diff_9_8 = list(set(key_for_9).symmetric_difference(set(key_for_8)))
        diff_1_4.append(diff_9_8[0])

        for idx, j in enumerate(updated_input_code):
            if len(j) == 6 and diff_1_4[0] in j and diff_1_4[1] in j and diff_1_4[2]:
                x = "".join(sorted(j))
                dic[x] = 6
                idx_to_rem3 = idx

        del updated_input_code[idx_to_rem3]
        # print(dic)

        # Checking for number 0
        for idx, j in enumerate(updated_input_code):
            if len(j) == 6:
                x = "".join(sorted(j))
                dic[x] = 0
                idx_to_rem4 = idx

        del updated_input_code[idx_to_rem4]

        # print(dic)

        # Checking for number 3, 5 and 2
        for idx, j in enumerate(updated_input_code):
            intersect_len = len(set(j).intersection(set(key_for_4)))
            if len(j) == 5 and intersect_len == 3 and key_for_1[0] in j and key_for_1[1] in j:
                x = "".join(sorted(j))
                dic[x] = 3
            elif len(j) == 5 and intersect_len == 3 and not (key_for_1[0] in j and key_for_1[1] in j):
                x = "".join(sorted(j))
                dic[x] = 5
            else:
                x = "".join(sorted(j))
                dic[x] = 2


        output_code_sorted = []
        for i in output_code:
            x = "".join(sorted(i))
            output_code_sorted.append(x)

        final_str = ""
        # print(dic)
        # Iterating through the output
        for i in output_code_sorted:
            final_str += str(dic[i])

        number = int(final_str)
        # print(number)

        total_number += number

    print(f'Solution for part 2: {total_number}')

Seven_Segment_Search("day8/day8_2021_input") # Time taken part 1: 15mins; Time taken part 2: ~3 hours





