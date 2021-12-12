import numpy as np

def dumboOctopus(file,part):

    list2d = []

    with open(file, 'r') as f:
        for line in f.readlines():
            list2d.append(list(line.rstrip('\n')))

    array2d = np.array(list2d).astype(np.int32)

    ttl_elements = array2d.shape[0] * array2d.shape[1]

    # Check all elements around the target element in array
    def check_num(i,j,arr):
        y = arr[i][j]
        lst = []

        if y >= 10:
            # print("FLASH:",(i,j),"y is :",y,"\n")

            # Check up
            try:
                x = (arr[i+1][j])
                if i+1>=0 and j>=0:
                    if arr[i+1][j] != 0:
                        arr[i+1][j] +=1
            except:
                pass

            # Check down
            try:
                x = (arr[i-1][j])
                if i-1>=0 and j>=0:
                    if arr[i-1][j] != 0:
                        arr[i-1][j] +=1
            except:
                pass

            # Check left
            try:
                x = (arr[i][j-1])
                if i>=0 and j-1>=0:
                    if arr[i][j-1] != 0:
                        arr[i][j-1] +=1
            except:
                pass

            # Check right
            try:
                x = (arr[i][j+1])
                if i>=0 and j+1>=0:
                    if arr[i][j+1] != 0:
                        arr[i][j+1] +=1
            except:
                pass

            # Check right up
            try:
                x = (arr[i+1][j+1])
                if i+1>=0 and j+1>=0:
                    if arr[i+1][j+1] != 0:
                        arr[i+1][j+1] +=1
            except:
                pass

            # Check right down
            try:
                x = (arr[i+1][j-1])
                if i+1>=0 and j-1>=0:
                    if arr[i+1][j-1] != 0:
                        arr[i+1][j-1] +=1
            except:
                pass

            # Check left up
            try:
                x = (arr[i-1][j+1])
                if i-1>=0 and j+1>=0:
                    if arr[i-1][j+1] != 0:
                        arr[i-1][j+1] +=1
            except:
                pass

            # Check left down
            try:
                x = (arr[i-1][j-1])
                if i-1>=0 and j-1>=0:
                    if arr[i-1][j-1] != 0:
                        arr[i-1][j-1] +=1
            except:
                pass

            arr[i][j] = 0

            # print(arr)

    if part == "part1":
        flash_count = 0
        for n in range(100):


            array2d += 1
            # Going through all the elements
            for i in range(len(array2d)):
                for j in range(len(array2d[i])):

                    # Check if there is a 10 in the array.
                    if ((array2d >= 10).sum()) > 0:
                        x,y = np.where(array2d >= 10)
                        # print(x,y)
                        for num in range(len(x)):
                            # print(x[num], y[num])
                            check_num(x[num],y[num],array2d)

                    check_num(i,j,array2d)

            # print("Step",n+1,": ","\n", array2d)
            flash_count += ((array2d == 0).sum())

        return(f'Solution for part 1: {flash_count}')

    else:
        for n in range(300):

            array2d += 1
            # Going through all the elements
            for i in range(len(array2d)):
                for j in range(len(array2d[i])):

                    # Check if there is a 10 in the array.
                    if ((array2d >= 10).sum()) > 0:
                        x,y = np.where(array2d >= 10)
                        # print(x,y)
                        for num in range(len(x)):
                            # print(x[num], y[num])
                            check_num(x[num],y[num],array2d)

                    check_num(i,j,array2d)

            # print("Step",n+1,": ","\n", array2d)

            if ((array2d == 0).sum() == ttl_elements):
                return(n+1)

print(dumboOctopus("day11/day11_2021_input", 'part2'))