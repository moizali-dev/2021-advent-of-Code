import numpy as np

def transparentOrigami(file, part = 'part1'):

    f = open(file, "r")

    max_x_coord = 0
    max_y_coord = 0
    master_coord_lst = []
    folds = []

    for i in f.readlines():
        lines = i.strip()
        if "," in lines:
            coord = lines.split(",")
            master_coord_lst.append([int(coord[0]), int(coord[1])])
            if int(coord[0]) > max_x_coord:
                max_x_coord = int(coord[0])
            if int(coord[1]) > max_y_coord:
                max_y_coord = int(coord[1])

        elif "=" in lines:
            fold = lines.split("=")
            folds.append([fold[0][-1],int(fold[1])])

    # Create an empty matrix
    arr = np.full((max_y_coord+1,max_x_coord+1), ['.'],dtype=str)

    # Adding the dots in the matrix
    for i in master_coord_lst:
        arr[i[1],i[0]] = "#"

    if part == 'part1':
        # Folds
        if folds[0][0] == "y":
            folds_line = folds[0][1]

            flipped_arr = np.flip(arr,0)[:folds_line]
            new_arr = arr[:folds_line]

            for iy, ix in np.ndindex(flipped_arr.shape):
                if flipped_arr[iy, ix] == '#' and new_arr[iy, ix] == '.':
                    new_arr[iy, ix] = '#'

            print((new_arr == '#').sum())

        if folds[0][0] == "x":
            folds_line = folds[0][1]

            flipped_arr = np.flip(arr,1)[:,:folds_line]
            new_arr = arr[:,:folds_line]

            for iy, ix in np.ndindex(flipped_arr.shape):
                if flipped_arr[iy, ix] == '#' and new_arr[iy, ix] == '.':
                    new_arr[iy, ix] = '#'

            print((new_arr == '#').sum())

    ## Part 2 solution ##
    if part == 'part2':
        for i in folds:
            # Folds
            if i[0] == "y":
                folds_line = i[1]

                flipped_arr = np.flip(arr,0)[:folds_line]
                new_arr = arr[:folds_line]

                for iy, ix in np.ndindex(flipped_arr.shape):
                    if flipped_arr[iy, ix] == '#' and new_arr[iy, ix] == '.':
                        new_arr[iy, ix] = '#'

                # print((new_arr == '#').sum())

            if i[0] == "x":
                folds_line = i[1]

                flipped_arr = np.flip(arr,1)[:,:folds_line]
                new_arr = arr[:,:folds_line]

                for iy, ix in np.ndindex(flipped_arr.shape):
                    if flipped_arr[iy, ix] == '#' and new_arr[iy, ix] == '.':
                        new_arr[iy, ix] = '#'

                # print((new_arr == '#').sum())

            arr = new_arr.copy()
            print("Fold",i,"completed")

    print(arr)

    # Convert to text file to be all in the same line

transparentOrigami("day13/day13_2021_input",'part2')
