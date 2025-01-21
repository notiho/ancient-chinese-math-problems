"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This problem involves solving a system of linear equations, which is described in the ancient Chinese "方程術" (method of solving simultaneous equations). Below is the Python implementation of the procedure described in the problem:


"""


from fractions import Fraction

# Step 1: Define the coefficients of the equations based on the problem
# White (白禾), Green (青禾), Yellow (黃禾), Black (黑禾)
# Each row represents the equation for each type of grain
# Coefficients for 白禾, 青禾, 黃禾, 黑禾
coefficients = [
    [1, -1, -1, 0],  # 白禾取青、黃
    [0, 1, -1, -1],  # 青禾取黃、黑
    [-1, 0, 1, -1],  # 黃禾取黑、白
    [-1, -1, 0, 1]   # 黑禾取白、青
]

# Step 2: Define the right-hand side of the equations (all sums equal 1斗)
rhs = [1, 1, 1, 1]

# Step 3: Solve the system of equations using the described method
# Initialize variables for 白禾, 青禾, 黃禾, 黑禾
白禾 = 青禾 = 黃禾 = 黑禾 = 0

# Using Gaussian elimination as described in the 方程術
# Normalize the first row
for i in range(4):
    coefficients[0][i] = Fraction(coefficients[0][i], coefficients[0][0])
rhs[0] = Fraction(rhs[0], coefficients[0][0])

# Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = coefficients[i][0]
    for j in range(4):
        coefficients[i][j] -= factor * coefficients[0][j]
    rhs[i] -= factor * rhs[0]

# Normalize the second row
for i in range(1, 4):
    coefficients[1][i] = Fraction(coefficients[1][i], coefficients[1][1])
rhs[1] = Fraction(rhs[1], coefficients[1][1])

# Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = coefficients[i][1]
    for j in range(1, 4):
        coefficients[i][j] -= factor * coefficients[1][j]
    rhs[i] -= factor * rhs[1]

# Normalize the third row
for i in range(2, 4):
    coefficients[2][i] = Fraction(coefficients[2][i], coefficients[2][2])
rhs[2] = Fraction(rhs[2], coefficients[2][2])

# Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = coefficients[i][2]
    for j in range(2, 4):
        coefficients[i][j] -= factor * coefficients[2][j]
    rhs[i] -= factor * rhs[2]

# Solve for the fourth variable
rhs[3] = Fraction(rhs[3], coefficients[3][3])

# Back-substitute to find the other variables
黑禾 = rhs[3]
黃禾 = rhs[2] - coefficients[2][3] * 黑禾
青禾 = rhs[1] - coefficients[1][2] * 黃禾 - coefficients[1][3] * 黑禾
白禾 = rhs[0] - coefficients[0][1] * 青禾 - coefficients[0][2] * 黃禾 - coefficients[0][3] * 黑禾

# Results
a, b = 1, 白禾
c, d = 1, 青禾
e, f = 1, 黃禾
g, h = 1, 黑禾


"""


### Explanation of the Results:
- `a, b`: White grain (白禾) steps and actual斗.
- `c, d`: Green grain (青禾) steps and actual斗.
- `e, f`: Yellow grain (黃禾) steps and actual斗.
- `g, h`: Black grain (黑禾) steps and actual斗.

Each variable represents the amount of grain (in steps and 斗) for each type of grain. The solution follows the ancient method of solving simultaneous equations as described in the problem.
"""


"""
Variable 'b' has wrong value. Expected: 11/37, Actual: -9/7
Variable 'd' has wrong value. Expected: 28/111, Actual: -11/7
Variable 'f' has wrong value. Expected: 17/111, Actual: -5/7
Variable 'h' has wrong value. Expected: 10/111, Actual: -13/7"""
