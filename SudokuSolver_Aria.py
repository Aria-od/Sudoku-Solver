#!/usr/bin/python3
# Aria Omidi
# CPS109 -- Assignment 1
# Sudoku solver
# using "backtracking" algorithm
# =======================================================
# Step 1:
# giving the data of the program which in this case is our sudoku board
# (I removed the input function to make the marker's work easier
#  as Mr.Harley said in his lectures)

# I used list to show my board
sudoboard = [
    [0, 0, 3, 0, 0, 4, 0, 5, 8],
    [6, 0, 0, 1, 0, 0, 0, 0, 2],
    [2, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 7, 9, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 8, 0, 3, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [3, 0, 5, 0, 0, 8, 0, 9, 0],
    [0, 2, 0, 0, 9, 0, 0, 0, 1],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
]


# =======================================================
# Step 2:
# we need to find empty slots or 0 in this case


def empty_finder(grid):
    for i in range(9):  # row
        for j in range(len(grid[0])):  # column
            if grid[i][j] == 0:
                return (i, j)  # i = row  j = column
    return None  # if it's not 0


# =======================================================
# Step 3:
# check the validity of a number in it's position
def validity_checker(numb, grid, position):
    # check the column
    for i in range(len(grid)):
        if grid[i][position[1]] == numb and position[0] != i:
            return False

    # check the row
    for i in range(len(grid[0])):
        if grid[position[0]][i] == numb and position[1] != i:
            return False

    # check the subgrids
    sub_x = position[1] // 3  # column of subgrids (i,x)
    sub_y = position[0] // 3  # row of subgrids (j,y)

    sub_x3 = sub_x * 3
    sub_y3 = sub_y * 3

    for i in range(sub_y3, sub_y3 + 3):
        # find the range of sub grid in row
        for j in range(sub_x3, sub_x3 + 3):
            # find the range of sub grid in column
            if grid[i][j] == numb and (i, j) != position:
                return False

    return True  # if the number is correct


# =======================================================
# Step 4:
# solver (main) function
# I wrote this function recursive


def sudo_solver(grid):
    # Base Case
    if not empty_finder(grid):
        return True  # this means there isn't any 0 left
    else:
        row, column = empty_finder(grid)  # i = row  j = column

    # general case
    # we should put one of the numbers between 1 to 9 in each space in sudoku
    for i in range(1, 10):
        # this will check whether the number is true or not
        if validity_checker(i, grid, (row, column)):
            grid[row][column] = i

            # here the function calls itself again to break
            if sudo_solver(grid):
                return True

            # this will make the number 0 again in the grid
            grid[row][column] = 0
    # this will make this function recursive
    return False


# =======================================================
# Step 5:
# print the board in a proper way
# (we can't just say "print(sudoboard)"
# because it is not gonna be like a real grid)


def printSuGrid(grid):
    for i in range(9):  # i in range of row
        if i % 3 == 0 and i != 0:
            print("==========================")
        for j in range(9):  # j in range of column
            if j % 3 == 0 and j != 0:
                print(" ‖ ", end=" ")
            if j == 8:
                print(grid[i][j])
            else:
                # this will change the list to string and print it
                print(str(grid[i][j]), "", end="")


# =======================================================
# Step 6:
# call the functions in order


printSuGrid(sudoboard)
print("\nStarted to solving please wait...\n")
sudo_solver(sudoboard)
printSuGrid(sudoboard)
