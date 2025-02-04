"""
今有上錦三疋中錦二疋下錦一疋直絹四十五疋上錦二疋中錦三疋下錦一疋直絹四十三疋上錦一疋中錦二疋下錦三疋直絹三十五疋問上中下錦各直絹幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰上錦一疋直絹 a疋 中錦一疋直絹 b疋 下錦一疋直絹 c疋
"""

"""
This problem involves solving a system of linear equations, which is described in the ancient Chinese "fangcheng" (method of solving simultaneous equations). The problem can be translated into Python code as follows:


"""

#----- content starts here -----

"""
Suppose there are:
- 3 bolts of upper-grade brocade, 2 bolts of middle-grade brocade, and 1 bolt of lower-grade brocade, worth 45 bolts of plain silk.
- 2 bolts of upper-grade brocade, 3 bolts of middle-grade brocade, and 1 bolt of lower-grade brocade, worth 43 bolts of plain silk.
- 1 bolt of upper-grade brocade, 2 bolts of middle-grade brocade, and 3 bolts of lower-grade brocade, worth 35 bolts of plain silk.

Question: How many bolts of plain silk is each bolt of upper-grade, middle-grade, and lower-grade brocade worth?

The procedure says: Use the method of "fangcheng" (simultaneous equations).
The answer says: 1 bolt of upper-grade brocade is worth *a* bolts of plain silk, 1 bolt of middle-grade brocade is worth *b* bolts of plain silk, and 1 bolt of lower-grade brocade is worth *c* bolts of plain silk.
"""

from fractions import Fraction

# Coefficients of the equations
# 3x + 2y + 1z = 45
# 2x + 3y + 1z = 43
# 1x + 2y + 3z = 35

# Step 1: Represent the equations as a matrix
matrix = [
    [3, 2, 1, 45],  # First equation
    [2, 3, 1, 43],  # Second equation
    [1, 2, 3, 35]   # Third equation
]

# Step 2: Eliminate the first variable (x) from the second and third equations
factor1 = Fraction(matrix[1][0], matrix[0][0])
for i in range(4):
    matrix[1][i] -= factor1 * matrix[0][i]

factor2 = Fraction(matrix[2][0], matrix[0][0])
for i in range(4):
    matrix[2][i] -= factor2 * matrix[0][i]

# Step 3: Eliminate the second variable (y) from the third equation
factor3 = Fraction(matrix[2][1], matrix[1][1])
for i in range(4):
    matrix[2][i] -= factor3 * matrix[1][i]

# Step 4: Back-substitution to solve for z, y, and x
z = Fraction(matrix[2][3], matrix[2][2])
y = Fraction(matrix[1][3] - matrix[1][2] * z, matrix[1][1])
x = Fraction(matrix[0][3] - matrix[0][2] * z - matrix[0][1] * y, matrix[0][0])

# Results
a = x  # Upper-grade brocade
b = y  # Middle-grade brocade
c = z  # Lower-grade brocade

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as a matrix where each row corresponds to an equation, and the last column represents the constants on the right-hand side.
2. **Gaussian Elimination**: The method of "fangcheng" is essentially Gaussian elimination. The first variable (`x`) is eliminated from the second and third equations, and then the second variable (`y`) is eliminated from the third equation.
3. **Back-Substitution**: Once the matrix is in upper triangular form, the variables are solved starting from the last equation and substituting back into the earlier equations.
4. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as required by the ancient method.

### Answer:
The values of `a`, `b`, and `c` represent the worth of 1 bolt of upper-grade, middle-grade, and lower-grade brocade in terms of bolts of plain silk, respectively.
"""


"""
"""
