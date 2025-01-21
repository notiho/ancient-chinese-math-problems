"""
今有上錦三疋中錦二疋下錦一疋直絹四十五疋上錦二疋中錦三疋下錦一疋直絹四十三疋上錦一疋中錦二疋下錦三疋直絹三十五疋問上中下錦各直絹幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗答曰上錦 a疋 直絹 b疋 中錦 c疋 直絹 d疋 下錦 e疋 直絹 f疋
"""

"""
This problem is a classic simultaneous equations problem, solved using the ancient Chinese "fangcheng" (方程) method, which is equivalent to solving linear equations. Let's translate the problem and procedure into Python code.

### Problem Explanation:
We are given three types of brocade (上錦, 中錦, 下錦) and their respective relationships to plain silk (直絹). The relationships are expressed as follows:

1. 3 units of 上錦, 2 units of 中錦, and 1 unit of 下錦 are equivalent to 45 units of plain silk.
2. 2 units of 上錦, 3 units of 中錦, and 1 unit of 下錦 are equivalent to 43 units of plain silk.
3. 1 unit of 上錦, 2 units of 中錦, and 3 units of 下錦 are equivalent to 35 units of plain silk.

The goal is to determine how many units of plain silk each unit of 上錦, 中錦, and 下錦 is worth.

### Procedure:
The "fangcheng" method involves systematically eliminating variables to solve for the unknowns. Below is the Python implementation.


"""


from fractions import Fraction

# Coefficients of the equations
# 3上錦 + 2中錦 + 1下錦 = 45
# 2上錦 + 3中錦 + 1下錦 = 43
# 1上錦 + 2中錦 + 3下錦 = 35

# Step 1: Represent the equations as a matrix
matrix = [
    [3, 2, 1, 45],  # First equation
    [2, 3, 1, 43],  # Second equation
    [1, 2, 3, 35]   # Third equation
]

# Step 2: Eliminate the first variable (上錦) from the second and third equations
for i in range(1, 3):
    factor = Fraction(matrix[i][0], matrix[0][0])
    for j in range(4):
        matrix[i][j] -= factor * matrix[0][j]

# Step 3: Eliminate the second variable (中錦) from the third equation
factor = Fraction(matrix[2][1], matrix[1][1])
for j in range(1, 4):
    matrix[2][j] -= factor * matrix[1][j]

# Step 4: Back-substitute to solve for 下錦, 中錦, and 上錦
下錦 = Fraction(matrix[2][3], matrix[2][2])
中錦 = Fraction(matrix[1][3] - matrix[1][2] * 下錦, matrix[1][1])
上錦 = Fraction(matrix[0][3] - matrix[0][2] * 下錦 - matrix[0][1] * 中錦, matrix[0][0])

# Results
a = 上錦
b = 1  # Each unit of 上錦 is worth `a` units of plain silk
c = 中錦
d = 1  # Each unit of 中錦 is worth `c` units of plain silk
e = 下錦
f = 1  # Each unit of 下錦 is worth `e` units of plain silk

# Output the results
a, b, c, d, e, f


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as a matrix where each row corresponds to an equation, and the last column represents the constants on the right-hand side.
2. **Elimination**: The first variable (上錦) is eliminated from the second and third equations by subtracting a scaled version of the first row. Similarly, the second variable (中錦) is eliminated from the third equation.
3. **Back-Substitution**: Once the matrix is in triangular form, the values of 下錦, 中錦, and 上錦 are computed by back-substitution.
4. **Results**: The values of 上錦, 中錦, and 下錦 are expressed as fractions to ensure precision.

### Answer:
The values of `a`, `b`, `c`, `d`, `e`, and `f` represent the worth of each type of brocade in terms of plain silk.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 9
Variable 'b' has wrong value. Expected: 9, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 7
Variable 'd' has wrong value. Expected: 7, Actual: 1
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 4, Actual: 1"""
