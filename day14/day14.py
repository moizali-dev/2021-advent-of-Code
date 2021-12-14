from tqdm import tqdm

def extendedPolymerization(file):

    dic = {}
    dic_input = {}
    poly = ""
    f = open(file,"r")
    for i in f.readlines():
        lines = i.strip()

        if "->" not in lines:
            poly += lines
        else:
            lines_split = lines.split(" -> ")
            dic[lines_split[0]] = lines_split[1]

    init_poly = '' + poly

    # logic for inserting polymer
    for x in tqdm(range(10)):
        poly_ins = ""
        for i in range(len(poly)-1):
            letters = poly[i:i+2]
            middle_letter = dic[letters]
            if i == 0:
                new_letters = letters[0] + middle_letter + letters[-1]
            else:
                new_letters = middle_letter + letters[-1]
            poly_ins += new_letters

        poly = poly_ins

    # Finding the highest and lowest element
    dic_count = {}
    for i in poly:
        if i not in dic_count:
            dic_count[i] = 1
        else:
            dic_count[i] += 1

    print(max(dic_count.values()) - min(dic_count.values()))

    # Using matrics to solve the problem
    print(dic)

extendedPolymerization("day14/day14_2021_input")

