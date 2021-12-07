import numpy as np

def the_Treachery_of_Whales(file, part2 = False):

    lines = np.loadtxt(file, delimiter=",")

    def sum_of_cons_int(n):
        return (n * (n-1)) / 2

    min_ttl = 1000000000
    for i in range(1, int(max(lines))+1):

        if part2 == False:
            new_lines = abs(lines - i)
        else:
            new_lines = sum_of_cons_int(abs(lines - i)+1)
        ttl = new_lines.sum()

        if ttl < min_ttl:
            min_ttl = ttl

    print(min_ttl)

the_Treachery_of_Whales("day7/day7_2021_input", False)
the_Treachery_of_Whales("day7/day7_2021_input", True)