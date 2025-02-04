"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "fangcheng" (方程) method. Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# 白禾二步、青禾三步、黃禾四步、黑禾五步
白禾 = 2
青禾 = 3
黃禾 = 4
黑禾 = 5

# 各取一步，實滿斗
滿斗 = 1

# 方程術
# Let x = 白禾一步實, y = 青禾一步實, z = 黃禾一步實, w = 黑禾一步實
# The equations based on the problem are:
# 2x + y + z = 1
# x + 3y + w = 1
# y + 4z + w = 1
# z + 5w + x = 1

# Coefficients matrix
A = [
    [2, 1, 1, 0],  # 2x + y + z = 1
    [1, 3, 0, 1],  # x + 3y + w = 1
    [0, 1, 4, 1],  # y + 4z + w = 1
    [1, 0, 1, 5],  # z + 5w + x = 1
]

# Constants vector
B = [1, 1, 1, 1]

# Step 1: Eliminate variables using Gaussian elimination
# Convert the matrix to upper triangular form
for i in range(4):
    for j in range(i + 1, 4):
        factor = Fraction(A[j][i], A[i][i])
        for k in range(4):
            A[j][k] -= factor * A[i][k]
        B[j] -= factor * B[i]

# Step 2: Back substitution to solve for variables
w = Fraction(B[3], A[3][3])
z = Fraction(B[2] - A[2][3] * w, A[2][2])
y = Fraction(B[1] - A[1][2] * z - A[1][3] * w, A[1][1])
x = Fraction(B[0] - A[0][1] * y - A[0][2] * z, A[0][0])

# Results
a = x  # 白禾一步實
b = y  # 青禾一步實
c = z  # 黃禾一步實
d = w  # 黑禾一步實

# Output the results
a, b, c, d
#----- content ends here -----


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is translated into a system of linear equations. Each equation represents the relationship between the steps of the different types of grains and their contributions to filling one dou.
2. **Gaussian Elimination**: The coefficients matrix is transformed into an upper triangular form to simplify solving the equations.
3. **Back Substitution**: Starting from the last variable, the values are calculated step by step.
4. **Fraction Handling**: The `Fraction` class is used to ensure precise calculations without floating-point errors.

### Answer:
The results `a`, `b`, `c`, and `d` represent the amount of dou for one step of 白禾, 青禾, 黃禾, and 黑禾 respectively.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 17/54
Variable 'b' has wrong value. Expected: 28/111, Actual: 7/36
Variable 'c' has wrong value. Expected: 17/111, Actual: 19/108
Variable 'd' has wrong value. Expected: 10/111, Actual: 11/108"""
