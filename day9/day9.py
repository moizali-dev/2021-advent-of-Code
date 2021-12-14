import numpy as np

def smokeBasin(file):

    f = open(file, "r")
    matrix = []
    for i in f.readlines():
        row = []
        for j in i.strip():
            row.append(int(j))
        matrix.append(row)

    arr = np.asarray(matrix)

    # Create function to check if the number is lowest for up, down, left and right

    def check_num(i,j,arr):
        y = arr[i][j]
        lst = []
        # Check up
        try:
            x = (arr[i+1][j])
            if i+1>=0 and j>=0:
                lst.append(x)
        except:
            pass

        # Check down
        try:
            x = (arr[i-1][j])
            if i-1>=0 and j>=0:
                lst.append(x)
        except:
            pass

        # Check left
        try:
            x = (arr[i][j-1])
            if i>=0 and j-1>=0:
                lst.append(x)
        except:
            pass

        # Check right
        try:
            x = (arr[i][j+1])
            if i>=0 and j+1>=0:
                lst.append(x)
        except:
            pass

    # Check for each element in arr
    lst = []
    lowest_point = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < min(check_num(i,j,arr)) :
                lst.append(arr[i][j])
                lowest_point.append((i,j))

    sol1 = (np.asarray(lst) + 1).sum()
    print(f'Solution for part 1: {sol1}')
    print(lowest_point)

print(smokeBasin("day9/day9_2021_input"))
