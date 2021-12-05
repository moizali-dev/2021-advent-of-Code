#############
### PartA ###
#############

import numpy as np
from timeit import default_timer as timer

def Hydrothermal_Venture(file):

    f = open(file, "r")

    coordinate_lst = []
    # Read lines and store the coordinates as tuple as k,v pairs in dictionary
    for i in f.readlines():

        line = i.strip()
        line_split = line.split(" -> ")
        start_coordinate = line_split[0]
        start_coordinate =start_coordinate.split(",")
        start_coordinate = tuple(map(int, start_coordinate))

        end_coordinate = line_split[1]
        end_coordinate =end_coordinate.split(",")
        end_coordinate = tuple(map(int, end_coordinate))

        coordinate_lst.append([start_coordinate, end_coordinate])

    # Remove all the coordinates that are not vertical
    for idx,i in enumerate(coordinate_lst):
        if not (i[0][0] == i[1][0] or i[0][1] == i[1][1]):
            coordinate_lst.remove(i)

    # Creating a matrix using numpy
    matrix = np.zeros((1000,1000))

    def update_matrix_points(start_coordinate, end_coordinate, matrix):
        # Condition if y1 = y2 then update
        if start_coordinate[1] == end_coordinate[1]:
            if start_coordinate[0] > end_coordinate[0]:
                for i in range(end_coordinate[0], start_coordinate[0]+1):
                    matrix[start_coordinate[1],i] += 1

            if start_coordinate[0] < end_coordinate[0]:
                for i in range(start_coordinate[0], end_coordinate[0]+1):
                    matrix[start_coordinate[1],i] += 1

        # Condition if x1 = z2 then update
        if start_coordinate[0] == end_coordinate[0]:
            if start_coordinate[1] > end_coordinate[1]:
                for i in range(end_coordinate[1], start_coordinate[1]+1):
                    matrix[i, start_coordinate[0]] += 1

            if start_coordinate[1] < end_coordinate[1]:
                for i in range(start_coordinate[1], end_coordinate[1]+1):
                    matrix[i, start_coordinate[0]] += 1
    #
    for i in coordinate_lst:
        update_matrix_points(i[0],i[1],matrix)

    count = 0
    for j in range(1000):
        for i in range(1000):
            if matrix[i][j] >= 2:
                count += 1

    return count

start = timer()
print(Hydrothermal_Venture("day5/day5_2021_input"))
end = timer()
print((end - start)*1000)

#############
### PartB ###
#############

def Hydrothermal_Venture_part2(file):

    f = open(file, "r")

    coordinate_lst = []
    # Read lines and store the coordinates as tuple as k,v pairs in dictionary
    for i in f.readlines():

        line = i.strip()
        line_split = line.split(" -> ")
        start_coordinate = line_split[0]
        start_coordinate =start_coordinate.split(",")
        start_coordinate = tuple(map(int, start_coordinate))

        end_coordinate = line_split[1]
        end_coordinate =end_coordinate.split(",")
        end_coordinate = tuple(map(int, end_coordinate))

        coordinate_lst.append([start_coordinate, end_coordinate])

    # Remove all the coordinates that are not vertical, horizontal and diagonal
    for idx,i in enumerate(coordinate_lst):
        vertical = i[0][0] == i[1][0]
        horitontal = i[0][1] == i[1][1]
        diagonal = abs(i[0][0] - i[1][0]) == abs(i[0][1] - i[1][1])
        if not ( vertical or horitontal or diagonal):
            coordinate_lst.remove(i)

    # Creating a matrix using numpy
    matrix = np.zeros((1000,1000))

    def update_matrix_points(start_coordinate, end_coordinate, matrix):
        # Condition if y1 = y2 then update
        if start_coordinate[1] == end_coordinate[1]:
            if start_coordinate[0] > end_coordinate[0]:
                for i in range(end_coordinate[0], start_coordinate[0]+1):
                    matrix[start_coordinate[1],i] += 1

            if start_coordinate[0] < end_coordinate[0]:
                for i in range(start_coordinate[0], end_coordinate[0]+1):
                    matrix[start_coordinate[1],i] += 1

        # Condition if x1 = x2 then update
        if start_coordinate[0] == end_coordinate[0]:
            if start_coordinate[1] > end_coordinate[1]:
                for i in range(end_coordinate[1], start_coordinate[1]+1):
                    matrix[i, start_coordinate[0]] += 1

            if start_coordinate[1] < end_coordinate[1]:
                for i in range(start_coordinate[1], end_coordinate[1]+1):
                    matrix[i, start_coordinate[0]] += 1

        # Condition for diagonal with negative gradient and moving up
        if start_coordinate[0] > end_coordinate[0] and start_coordinate[1] > end_coordinate[1]:
            distance = abs(start_coordinate[0] - end_coordinate[0])
            for i in range(distance + 1):
                matrix[start_coordinate[1] - i, start_coordinate[0] - i] += 1

        # Condition for diagonal with negative gradient and moving down
        if start_coordinate[0] < end_coordinate[0] and start_coordinate[1] < end_coordinate[1]:
            distance = abs(start_coordinate[0] - end_coordinate[0])
            for i in range(distance + 1):
                matrix[start_coordinate[1] + i, start_coordinate[0] + i] += 1

        # Condition for diagonal with positive gradient and moving down
        if start_coordinate[0] > end_coordinate[0] and start_coordinate[1] < end_coordinate[1]:
            distance = abs(start_coordinate[0] - end_coordinate[0])
            for i in range(distance + 1):
                matrix[start_coordinate[1] + i, start_coordinate[0] - i] += 1

        # Condition for diagonal with positive gradient and moving down
        if start_coordinate[0] < end_coordinate[0] and start_coordinate[1] > end_coordinate[1]:
            distance = abs(start_coordinate[0] - end_coordinate[0])
            for i in range(distance + 1):
                matrix[start_coordinate[1] - i, start_coordinate[0] + i] += 1


    for i in coordinate_lst:
        update_matrix_points(i[0],i[1],matrix)

    count = 0
    for j in range(1000):
        for i in range(1000):
            if matrix[i][j] >= 2:
                count += 1

    return count

start = timer()
print(Hydrothermal_Venture_part2("day5/day5_2021_input"))
end = timer()
print((end - start)*1000)