def read_matrix():
    rows, cols = map(int, input("Enter matrix size: > ").split())
    matrix = []
    print("Enter matrix:")
    for _ in range(rows):
        row = list(map(float, input("> ").split()))
        matrix.append(row)
    return matrix


def format_number(number):
    if abs(number - round(number)) < 1e-10:
        return str(int(round(number)))
    return f"{number:.2f}".rstrip("0").rstrip(".")


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(format_number(x) for x in row))


def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def multiply_matrix_by_constant(matrix, constant):
    return [
        [element * constant for element in row]
        for row in matrix
    ]


def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        return None

    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            value = sum(a[i][k] * b[k][j] for k in range(len(b)))
            row.append(value)
        result.append(row)
    return result


def transpose_main_diagonal(matrix):
    return [list(row) for row in zip(*matrix)]


def transpose_side_diagonal(matrix):
    n = len(matrix)
    return [
        [matrix[n - 1 - j][n - 1 - i] for j in range(n)]
        for i in range(n)
    ]


def transpose_vertical(matrix):
    return [row[::-1] for row in matrix]


def transpose_horizontal(matrix):
    return matrix[::-1]


def transpose_operation():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")

    choice = input("Your choice: > ")
    matrix = read_matrix()

    if choice == "1":
        result = transpose_main_diagonal(matrix)
    elif choice == "2":
        result = transpose_side_diagonal(matrix)
    elif choice == "3":
        result = transpose_vertical(matrix)
    elif choice == "4":
        result = transpose_horizontal(matrix)
    else:
        print("Invalid choice!")
        return

    print_matrix(result)


def calculate_determinant(matrix):
    n = len(matrix)

    if any(len(row) != n for row in matrix):
        return None

    a = [row[:] for row in matrix]
    determinant = 1

    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(a[r][i]))

        if abs(a[pivot][i]) < 1e-10:
            return 0

        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            determinant *= -1

        pivot_value = a[i][i]
        determinant *= pivot_value

        for j in range(i + 1, n):
            factor = a[j][i] / pivot_value
            for k in range(i + 1, n):
                a[j][k] -= factor * a[i][k]
            a[j][i] = 0

    return determinant


def inverse_matrix(matrix):
    n = len(matrix)

    if any(len(row) != n for row in matrix):
        return None

    a = [
        matrix[i][:] + [1.0 if i == j else 0.0 for j in range(n)]
        for i in range(n)
    ]

    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(a[r][i]))

        if abs(a[pivot][i]) < 1e-10:
            return None

        a[i], a[pivot] = a[pivot], a[i]

        pivot_value = a[i][i]
        a[i] = [value / pivot_value for value in a[i]]

        for j in range(n):
            if j != i:
                factor = a[j][i]
                a[j] = [
                    a[j][k] - factor * a[i][k]
                    for k in range(2 * n)
                ]

    return [row[n:] for row in a]


def determinant_operation():
    matrix = read_matrix()
    determinant = calculate_determinant(matrix)

    if determinant is None:
        print("ERROR")
    else:
        print(format_number(determinant))


def inverse_operation():
    matrix = read_matrix()
    result = inverse_matrix(matrix)

    if result is None:
        print("This matrix doesn't have an inverse.")
    else:
        print_matrix(result)


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")

        choice = input("Your choice: > ")

        if choice == "0":
            break

        elif choice == "1":
            print("Enter first matrix:")
            a = read_matrix()
            print("Enter second matrix:")
            b = read_matrix()
            result = add_matrices(a, b)
            if result is None:
                print("ERROR")
            else:
                print_matrix(result)

        elif choice == "2":
            matrix = read_matrix()
            constant = float(input("Enter constant: > "))
            print_matrix(multiply_matrix_by_constant(matrix, constant))

        elif choice == "3":
            print("Enter first matrix:")
            a = read_matrix()
            print("Enter second matrix:")
            b = read_matrix()
            result = multiply_matrices(a, b)
            if result is None:
                print("ERROR")
            else:
                print_matrix(result)

        elif choice == "4":
            transpose_operation()

        elif choice == "5":
            determinant_operation()

        elif choice == "6":
            inverse_operation()

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
