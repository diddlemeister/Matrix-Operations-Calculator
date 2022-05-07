# Matrix Calculator App by Edward Roy

def setup():
    print("Enter the amount of matrixes (max 2): ")
    matrix_amount = '0'
    while matrix_amount != '1' and matrix_amount != '2':
        matrix_amount = input()
        if matrix_amount != '1' and matrix_amount != '2':
            print("Invalid Matrix Value. Please try again:")
    if matrix_amount == '1':
        return 1
    elif matrix_amount == '2':
        return 2
    else:
        return 0


def create_matrix():
    print("Enter size of matrix (in the form AxB): ")
    matrix_size = input()
    split = matrix_size.index('x')
    rows = int(matrix_size[0:split])
    cols = int(matrix_size[split + 1:])
    matrix_list = []
    print("Enter matrix values: ")
    for i in range(0, rows):
        row_list = []
        for j in range(0, cols):
            cont = True
            validity = True
            while cont is True:
                value = input()
                validity = True
                for i in value:
                    if i not in '1234567890':
                        validity = False
                if validity == True:
                    row_list.append(int(value))
                    cont = False
                else:
                    print("Invalid Input. Please try again:")
        matrix_list.append(row_list)
    return matrix_list

def print_matrix(matrix):
    for i in matrix:
        print(i)

def dot_product(matrix1, matrix2, i, j):
    sum = 0
    for x in range(0, len(matrix1[i])):
        sum += matrix1[i][x] * matrix2[x][j]
    return sum

def multiply_matrix(matrix1, matrix2):
    if len(matrix2) != 0:
        if len(matrix1) == len(matrix2[0]):
            new_matrix = []
            for i in range(0, len(matrix1)):
                new_matrix_row = []
                for j in range(0, len(matrix2[0])):
                    new_matrix_row.append(dot_product(matrix1, matrix2, i, j))
                new_matrix.append(new_matrix_row)
        else:
            print("Matrices not multiplicable.")
            new_matrix = []
    else:
        print("Not enough data.")
        new_matrix = []
    return new_matrix

def input_number():
    power = ''
    repeat = True
    while repeat:
        power = input()
        validity = True
        for i in power:
            if i not in '1234567890.':
                validity = False
        if validity == True:
            power = float(power)
            repeat = False
        else:
            print("Invalid Input. Please try again:")
    return power

def scale_matrix(matrix1, scale):
    new_matrix = []
    for i in matrix1:
        new_row = []
        for j in i:
            new_row.append(j*scale)
        new_matrix.append(new_row)
    return new_matrix

#
# MAIN FUNCTION VVVVVVV
# -----------------------------------------------------------------------------------------------------
def run():
    a = setup()
    if a == 1:
        matrix_1 = create_matrix()
        matrix_2 = []
        print_matrix(matrix_1)
    elif a == 2:
        matrix_1 = create_matrix()
        print_matrix(matrix_1)
        matrix_2 = create_matrix()
        print_matrix(matrix_2)
    else:
        matrix_1 = []
        matrix_2 = []

    cont = True
    while cont is True:
        print("")
        print("Enter command:")
        print("(Type 'help' for more info.)")
        command = input()
        if command == 'quit':
            cont = False
            print("Thank you for using this app!")
            return 0

        elif command == "multiply":
            multiplied_matrix = multiply_matrix(matrix_1, matrix_2)
            if len(multiplied_matrix) != 0:
                print_matrix(multiplied_matrix)

        elif command == "add":
            print('')

        elif command == "scale":
            print('To what scalar would you like to multiply the matrix to: ')
            scalar = input_number()
            scaled_matrix = scale_matrix(matrix_1, scalar)
            print_matrix(scaled_matrix)

        elif command == "power":
            if len(matrix_1) == len(matrix_1[0]):
                print("Please enter the number you would like to power the matrix to:")
                power = input_number()
                powered_matrix = matrix_1
                for i in range(0, power-1):
                    powered_matrix = multiply_matrix(powered_matrix, matrix_1)
                print_matrix(powered_matrix)
            else:
                print("Invalid Matrix Size. Cannot be powered.")

        elif command == "help":
            print("Help")
            print("-------------------------------------------------------------------")
            print("- Use \"multiply\" to multiply Matrix 1 and Matrix 2 together.")
            print("- Use \"add\" to add Matrix 1 and Matrix 2 together.")
            print("- Use \"scale\" to multiply Matrix 1 by a scalar.")
            print("- Use \"power\" to multiply Matrix 1 to a certain power.")
            print("- Use \"quit\" to exit the program.")
            print("Thank you, again, for using this program.")
            print("-------------------------------------------------------------------")


# -----------------------------------------------------------------------------------------------------

run()

