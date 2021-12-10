from numpy import median

def syntaxScoring(file):

    f = open(file, "r")

    open_symbol = ["[","(","{","<"]
    close_dic = {"]" : "[" , ">" : "<" , "}" : "{" , ")" : "("}
    score = {")": 3 , "]": 57, "}": 1197, ">": 25137}

    frst_corr = []
    master_lst = []
    for i in f.readlines():
        line = i.split()

        lst = []
        for idx, j in enumerate(line[0]):
            if j in open_symbol:
                lst.append(j)
            else:
                lst.append(j)
                if close_dic[j] == lst[len(lst) - 2]:
                    lst = lst[:-2]
                else:
                    frst_corr.append((j, lst[len(lst) - 2]))
                    lst = []
                    break

        master_lst.append(lst)

    sum = 0
    for i in frst_corr:
        sum += score[i[0]]

    print(f'Solution for part 1: {sum}')

    lst_sum_ttl = []
    score_p2 = {")":1,"]":2,"}":3,">":4}
    open_dic = {"[" : "]" , "<" : ">" , "{" : "}" , "(" : ")"}
    for i in master_lst:
        sum = 0
        if len(i) != 0:
            for j in i[::-1]:
                sum *= 5
                symbl = open_dic[j]
                sum += score_p2[symbl]
            lst_sum_ttl.append(sum)

    part2_sum = (median(lst_sum_ttl))
    print(f'Solution for part 2: {part2_sum}')

print(syntaxScoring("day10/day10_2021_input"))