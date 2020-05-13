# Doomsday Fuel
# =============

# Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel. 

# Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).  You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms that the ore can become, but you haven't seen all of them.

# Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly. 

# For example, consider the matrix m:
# [
#   [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
#   [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
#   [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
#   [0,0,0,0,0,0],  # s3 is terminal
#   [0,0,0,0,0,0],  # s4 is terminal
#   [0,0,0,0,0,0],  # s5 is terminal
# ]
# So, we can consider different paths to terminal states, such as:
# s0 -> s1 -> s3
# s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
# s0 -> s1 -> s0 -> s5
# Tracing the probabilities of each, we find that
# s2 has probability 0
# s3 has probability 3/14
# s4 has probability 1/7
# s5 has probability 9/14
# So, putting that together, and making a common denominator, gives an answer in the form of
# [s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
# [0, 3, 2, 9, 14].

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution({{0, 2, 1, 0, 0}, {0, 0, 0, 3, 4}, {0, 0, 0, 0, 0}, {0, 0, 0, 0,0}, {0, 0, 0, 0, 0}})
# Output:
#     [7, 6, 8, 21]

# Input:
# Solution.solution({{0, 1, 0, 0, 0, 1}, {4, 0, 0, 3, 2, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}})
# Output:
#     [0, 3, 2, 9, 14]

# -- Python cases --
# Input:
# solution.solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
# Output:
#     [7, 6, 8, 21]

# Input:
# solution.solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# Output:
#     [0, 3, 2, 9, 14]
from fractions import Fraction
from fractions import gcd

def solution(m):
    terminal_states = []
    non_terminal_states = []
    for i, arr in enumerate(m) :
        if all([num == 0 for num in arr]) :
            terminal_states.append(i)
        else :
            non_terminal_states.append(i)
    transform(m)
    Q = matrix_slice(m, non_terminal_states, non_terminal_states)
    R = matrix_slice(m, non_terminal_states, terminal_states)
    F = matrix_inverse(matrix_substract(identify_matrix(len(Q)), Q))
    ans = matrix_multiplication(F, R)
    denominator = array_lcm([num.denominator for num in ans[0]])
    ans = [num.numerator * denominator // num.denominator for num in ans[0]]
    ans.append(denominator)
    return ans
def array_lcm(arr) :
    if arr < 2 : return arr[0]
    ans = 1
    for num in arr :
        ans = lcm(ans, num)
    return ans
def lcm(x, y) :
    return x * y // gcd(x, y)
def matrix_inverse(A) :
    n = len(A)
    assert(n == len(A[0]))
    inverse = identify_matrix(n)
    for col in range(n):
        diagonal_row = col
        assert(A[diagonal_row][col] != 0)
        k = Fraction(1, A[diagonal_row][col])
        A = multiply_row_of_square_matrix(A, diagonal_row, k)
        inverse = multiply_row_of_square_matrix(inverse, diagonal_row, k)
        source_row = diagonal_row
        for target_row in range(n):
            if source_row != target_row:
                k = -A[target_row][col]
                A = add_multiple_of_row_of_square_matrix(A, source_row, k, target_row)
                inverse = add_multiple_of_row_of_square_matrix(inverse, source_row, k, target_row)
    return inverse
def add_multiple_of_row_of_square_matrix(A, source_row, k, target_row):
    n = len(A)
    row_operator = identify_matrix(n)
    row_operator[target_row][source_row] = k
    return matrix_multiplication(row_operator, A)
def multiply_row_of_square_matrix(A, row, k):
    n = len(A)
    row_operator = identify_matrix(n)
    row_operator[row][row] = k
    return matrix_multiplication(row_operator, A)
def matrix_multiplication(A, B) :
    A_rows = len(A)
    A_cols = len(A[0])
    B_cols = len(B[0])
    C = make_matrix(A_rows, B_cols)
    # now find each value in turn in the result matrix
    for row in range(A_rows):
        for col in range(B_cols):
            dot_product = Fraction(0, 1)
            for i in range(A_cols):
                dot_product += A[row][i]*B[i][col]
            C[row][col] = dot_product
    return C
def matrix_substract(A, B):
    m, n = len(A), len(A[0])
    ans = make_matrix(m, n)
    for i in range(m) :
        for j in range(n) :
            ans[i][j] = A[i][j] - B[i][j]
    return ans
def identify_matrix(n) :
    ans = make_matrix(n, n)
    for i in range(n) :
        ans[i][i] = 1
    return ans
def make_matrix(m, n) :
    ans = [[0 for _ in range(n)] for _ in range(m)]
    return ans
def transform(matrix) :
    for i, arr in enumerate(matrix) :
        if all([num == 0 for num in arr]) :
            matrix[i][i] = 1
        else :
            _sum = sum(arr)
            for j, val in enumerate(arr) :
                matrix[i][j] = Fraction(val, _sum)
def matrix_slice(matrix, rows, cols) :
    new_matrix = []
    for row in rows :
        new_row = []
        for col in cols :
            new_row.append(matrix[row][col])
        new_matrix.append(new_row)
    return new_matrix


# m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# nn = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
# print(solution(m))
# print(solution(nn))

from fractions import gcd
from fractions import Fraction


def multiply_matrices(a, b):
    a_rows = len(a)
    a_cols = len(a[0])
    b_cols = len(b[0])
    rows = a_rows
    cols = b_cols
    c = make_2d_list(rows, cols)
    for row in range(rows):
        for col in range(cols):
            dot_product = Fraction(0, 1)
            for i in range(a_cols):
                dot_product += a[row][i]*b[i][col]
            c[row][col] = dot_product
    return c


def multiply_row_of_square_matrix(m, row, k):
    n = len(m)
    row_operator = make_identity(n)
    row_operator[row][row] = k
    return multiply_matrices(row_operator, m)


def make_2d_list(rows, cols):
    a = []
    for row in range(rows):
        a += [[0] * cols]
    return a


def make_identity(n):
    result = make_2d_list(n, n)
    for i in range(n):
        result[i][i] = Fraction(1, 1)
    return result


def add_multiple_of_row_of_square_matrix(m, source_row, k, target_row):
    # add k * source_row to target_row of matrix m
    n = len(m)
    row_operator = make_identity(n)
    row_operator[target_row][source_row] = k
    return multiply_matrices(row_operator, m)


def invert_matrix(m):
    n = len(m)
    assert(len(m) == len(m[0]))
    inverse = make_identity(n)
    for col in range(n):
        diagonal_row = col
        assert(m[diagonal_row][col] != 0)
        k = Fraction(1, m[diagonal_row][col])
        m = multiply_row_of_square_matrix(m, diagonal_row, k)
        inverse = multiply_row_of_square_matrix(inverse, diagonal_row, k)
        source_row = diagonal_row
        for target_row in range(n):
            if source_row != target_row:
                k = -m[target_row][col]
                m = add_multiple_of_row_of_square_matrix(m, source_row, k, target_row)
                inverse = add_multiple_of_row_of_square_matrix(inverse, source_row, k, target_row)
    return inverse


def subtract_identity(q, denominator):
    size = range(len(q))
    for i in size:
        for j in size:
            if i == j:
                q[i][j] = denominator - q[i][j]
            else:
                q[i][j] = - q[i][j]


def transform_matrix(m):
    for row_index, row in enumerate(m):
        row_sum = sum(m[row_index])
        if row_sum == 0:
            m[row_index][row_index] = 1
        else:
            for col_index, col in enumerate(row):
                m[row_index][col_index] = Fraction(col, row_sum)


def get_submatrix(m, rows, cols):
    new_matrix = []

    for row in rows:
        current_row = []
        for col in cols:
            current_row.append(m[row][col])
        new_matrix.append(current_row)
    return new_matrix


# def get_q(m, non_terminal_states):
#     return get_submatrix(m, non_terminal_states, non_terminal_states)


# def get_r(m, non_terminal_states, terminal_states):
#     return get_submatrix(m, non_terminal_states, terminal_states)


def subtract_matrices(a, b):
    new_matrix = []
    for row_index, row in enumerate(a):
        column = []
        for col_index, col in enumerate(row):
            column.append(a[row_index][col_index] - b[row_index][col_index])
        new_matrix.append(column)

    return new_matrix


def lcm(a, b):
    result = a * b / gcd(a, b)

    return result


def lcm_for_arrays(args):
    array_length = len(args)
    if array_length <= 2:
        return lcm(*args)

    initial = lcm(args[0], args[1])
    i = 2
    while i < array_length:
        initial = lcm(initial, args[i])
        i += 1
    return initial


def answer(m):
    terminal_states = []
    non_terminal_states = []
    for index, row in enumerate(m):
        if sum(row) == 0:
            terminal_states.append(index)
        else:
            non_terminal_states.append(index)

    if len(terminal_states) == 1:
        return [1, 1]

    transform_matrix(m)

    Q = get_submatrix(m, non_terminal_states, non_terminal_states)
    R = get_submatrix(m, non_terminal_states, terminal_states)
    F = invert_matrix(subtract_matrices(make_identity(len(Q)), Q))

    ans = multiply_matrices(F, R)

    denominator = lcm_for_arrays([item.denominator for item in ans[0]])

    ans = [item.numerator * denominator / item.denominator for item in ans[0]]

    ans.append(denominator)

    return ans

m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
nn = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
print(answer(m))
print(answer(nn))