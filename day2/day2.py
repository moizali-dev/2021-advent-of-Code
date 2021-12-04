#############
### DAY 2 ###
#############

def horizontal_depth_product(file):

    f = open(file, "r")

    horizontal, depth, aim = 0, 0

    for i in f.readlines():
        j = (i.strip().split(" "))
        if j[0] == "forward":
            horizontal += int(j[1])
        elif j[0] == "up":
            depth -= int(j[1])
        elif j[0] == "down":
            depth += int(j[1])

    return (horizontal * depth)

def horizontal_depth_product_aim(file):

    f = open(file, "r")

    horizontal, depth, aim = 0, 0, 0

    for i in f.readlines():
        j = (i.strip().split(" "))
        if j[0] == "forward":
            horizontal += int(j[1])
            depth += (aim * int(j[1]))
        elif j[0] == "up":
            aim -= int(j[1])
        elif j[0] == "down":
            aim += int(j[1])

    return (horizontal * depth)

print(horizontal_depth_product("day2/day2_2021_input"))
print(horizontal_depth_product_aim("day2/day2_2021_input"))