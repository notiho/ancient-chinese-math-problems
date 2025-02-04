"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
To solve this problem using the described ancient Chinese method (方程術), we will translate the procedure into Python code step by step. The problem essentially involves solving a system of linear equations.

The equations are derived from the problem statement:
1. White (白禾) takes from Green (青禾) and Yellow (黃禾).
2. Green (青禾) takes from Yellow (黃禾) and Black (黑禾).
3. Yellow (黃禾) takes from Black (黑禾) and White (白禾).
4. Black (黑禾) takes from White (白禾) and Green (青禾).

Each type of grain contributes to a total of 1斗 (full斗). Let the amounts of 白禾, 青禾, 黃禾, and 黑禾 per step be `a`, `b`, `c`, and `d`, respectively. The equations can be written as:

- \( a + b + c = 1 \)
- \( b + c + d = 1 \)
- \( c + d + a = 1 \)
- \( d + a + b = 1 \)

We will solve this system of equations using the described method.


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the coefficients of the equations
# Each row corresponds to an equation: [a, b, c, d, total]
matrix = [
    [1, 1, 1, 0, 1],  # a + b + c = 1
    [0, 1, 1, 1, 1],  # b + c + d = 1
    [1, 0, 1, 1, 1],  # c + d + a = 1
    [1, 1, 0, 1, 1]   # d + a + b = 1
]

# Step 2: Perform Gaussian elimination
# Normalize the first row
for i in range(4):
    matrix[0][i] = Fraction(matrix[0][i], matrix[0][0])
matrix[0][4] = Fraction(matrix[0][4], matrix[0][0])

# Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = matrix[i][0]
    for j in range(5):
        matrix[i][j] -= factor * matrix[0][j]

# Normalize the second row
for i in range(1, 4):
    matrix[1][i] = Fraction(matrix[1][i], matrix[1][1])
matrix[1][4] = Fraction(matrix[1][4], matrix[1][1])

# Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = matrix[i][1]
    for j in range(5):
        matrix[i][j] -= factor * matrix[1][j]

# Normalize the third row
for i in range(2, 4):
    matrix[2][i] = Fraction(matrix[2][i], matrix[2][2])
matrix[2][4] = Fraction(matrix[2][4], matrix[2][2])

# Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = matrix[i][2]
    for j in range(5):
        matrix[i][j] -= factor * matrix[2][j]

# Normalize the fourth row
matrix[3][3] = Fraction(matrix[3][3], matrix[3][3])
matrix[3][4] = Fraction(matrix[3][4], matrix[3][3])

# Back-substitute to find the values of a, b, c, d
d = matrix[3][4]
c = matrix[2][4] - matrix[2][3] * d
b = matrix[1][4] - matrix[1][2] * c - matrix[1][3] * d
a = matrix[0][4] - matrix[0][1] * b - matrix[0][2] * c - matrix[0][3] * d

# Results
a斗 = a
b斗 = b
c斗 = c
d斗 = d

# Output the results
a斗, b斗, c斗, d斗
#----- content ends here -----


"""


### Explanation:
1. The system of equations is represented as a matrix.
2. Gaussian elimination is used to solve the system step by step, following the ancient method of elimination and substitution.
3. The final values of `a`, `b`, `c`, and `d` represent the amount of each type of grain per step.

### Answer:
- 白禾一步實 \( a斗 \)
- 青禾一步實 \( b斗 \)
- 黃禾一步實 \( c斗 \)
- 黑禾一步實 \( d斗 \)
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 1
Variable 'b' has wrong value. Expected: 28/111, Actual: 1
Variable 'c' has wrong value. Expected: 17/111, Actual: -1
Variable 'd' has wrong value. Expected: 10/111, Actual: 1"""
