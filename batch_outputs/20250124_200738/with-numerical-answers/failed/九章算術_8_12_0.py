"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a(=721/100)丈 。甲綆長 b(=53/20)丈 ，乙綆長 c(=191/100)丈 ，丙綆長 d(=37/25)丈 ，丁綆長 e(=129/100)丈 ，戊綆長 f(=38/5)尺 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "fangcheng" (方程) method, which is an early form of solving linear equations. Below is the Python implementation of the problem using the described procedure.


"""

#----- content starts here -----

from fractions import Fraction

# Define the coefficients for the equations based on the problem:
# Each equation represents the relationship between the lengths of the ropes (綆) and the depth of the well (井深).
# Let the depth of the well be `井深 = x` and the lengths of the ropes for each family be `甲 = a`, `乙 = b`, `丙 = c`, `丁 = d`, `戊 = e`.

# Coefficients for the equations:
# 甲: x = a + 2
# 乙: x = b + 3
# 丙: x = c + 4
# 丁: x = d + 5
# 戊: x = e + 6
# Additionally, e = a + 6 (戊六綆不足，如甲一綆)

# Rewrite the equations in terms of `x`:
# x - a = 2
# x - b = 3
# x - c = 4
# x - d = 5
# x - e = 6
# e - a = 6

# Using fangcheng (linear equations), we solve for `x`, `a`, `b`, `c`, `d`, `e`.

# Step 1: Represent the system of equations in matrix form:
# Coefficient matrix:
# |  1  -1   0   0   0   0 |   2
# |  1   0  -1   0   0   0 |   3
# |  1   0   0  -1   0   0 |   4
# |  1   0   0   0  -1   0 |   5
# |  1   0   0   0   0  -1 |   6
# |  0   1   0   0   0  -1 |   6

# Augmented matrix:
matrix = [
    [1, -1,  0,  0,  0,  0,  2],
    [1,  0, -1,  0,  0,  0,  3],
    [1,  0,  0, -1,  0,  0,  4],
    [1,  0,  0,  0, -1,  0,  5],
    [1,  0,  0,  0,  0, -1,  6],
    [0,  1,  0,  0,  0, -1,  6]
]

# Step 2: Perform Gaussian elimination to solve the system of equations.

# Function to perform Gaussian elimination
def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Forward elimination
    for i in range(rows):
        # Normalize the pivot row
        pivot = matrix[i][i]
        for j in range(i, cols):
            matrix[i][j] = Fraction(matrix[i][j], pivot)

        # Eliminate the current column in the rows below
        for k in range(i + 1, rows):
            factor = matrix[k][i]
            for j in range(i, cols):
                matrix[k][j] -= factor * matrix[i][j]

    # Back substitution
    for i in range(rows - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            factor = matrix[k][i]
            for j in range(i, cols):
                matrix[k][j] -= factor * matrix[i][j]

    # Extract solutions
    solutions = [matrix[i][-1] for i in range(rows)]
    return solutions

# Solve the system of equations
solutions = gaussian_elimination(matrix)

# Extract the solutions
井深 = solutions[0]  # Depth of the well
甲綆 = solutions[1]  # Length of rope for 甲
乙綆 = solutions[2]  # Length of rope for 乙
丙綆 = solutions[3]  # Length of rope for 丙
丁綆 = solutions[4]  # Length of rope for 丁
戊綆 = solutions[5]  # Length of rope for 戊

# Convert the results to the required units (丈 and 尺)
a = 井深  # Depth of the well in 丈
b = 甲綆  # Length of rope for 甲 in 丈
c = 乙綆  # Length of rope for 乙 in 丈
d = 丙綆  # Length of rope for 丙 in 丈
e = 丁綆  # Length of rope for 丁 in 丈
f = 戊綆 * 10  # Length of rope for 戊 in 尺 (1 丈 = 10 尺)

# Output the results
井深 = a  # 721/100 丈
甲綆 = b  # 53/20 丈
乙綆 = c  # 191/100 丈
丙綆 = d  # 37/25 丈
丁綆 = e  # 129/100 丈
戊綆 = f  # 38/5 尺
#----- content ends here -----


"""

"""


"""
Code error: Fraction(0, 0)"""
