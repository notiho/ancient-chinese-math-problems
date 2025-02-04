"""
今有上錦三疋中錦二疋下錦一疋直絹四十五疋上錦二疋中錦三疋下錦一疋直絹四十三疋上錦一疋中錦二疋下錦三疋直絹三十五疋問上中下錦各直絹幾何
術曰如方程
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
答曰上錦一疋直絹 a疋 中錦一疋直絹 b疋 下錦一疋直絹 c疋
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method described in the "fangcheng" (方程) procedure. The problem is essentially asking for the value of each type of silk (upper, middle, and lower) in terms of plain silk.

### Problem Restatement:
There are three types of silk: upper silk (上錦), middle silk (中錦), and lower silk (下錦). Their values in terms of plain silk (直絹) are given in three equations:
1. 3 upper silk + 2 middle silk + 1 lower silk = 45 plain silk
2. 2 upper silk + 3 middle silk + 1 lower silk = 43 plain silk
3. 1 upper silk + 2 middle silk + 3 lower silk = 35 plain silk

We are tasked to find how much plain silk (直絹) each type of silk (上錦, 中錦, 下錦) is worth.

### Fangcheng Procedure:
The procedure involves systematically eliminating variables using multiplication and subtraction, similar to Gaussian elimination in modern algebra.

### Implementation in Python:


"""


from fractions import Fraction

# Coefficients of the equations
# Equation 1: 3上 + 2中 + 1下 = 45
# Equation 2: 2上 + 3中 + 1下 = 43
# Equation 3: 1上 + 2中 + 3下 = 35

# Initialize the matrix (augmented matrix for the system of equations)
matrix = [
    [3, 2, 1, 45],  # Row 1
    [2, 3, 1, 43],  # Row 2
    [1, 2, 3, 35]   # Row 3
]

# Step 1: Normalize the first row by dividing by the first coefficient (3)
factor = matrix[0][0]
matrix[0] = [Fraction(x, factor) for x in matrix[0]]

# Step 2: Eliminate the first variable (上錦) from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    matrix[i] = [matrix[i][j] - factor * matrix[0][j] for j in range(4)]

# Step 3: Normalize the second row by dividing by the second coefficient (new coefficient of 中錦)
factor = matrix[1][1]
matrix[1] = [Fraction(x, factor) for x in matrix[1]]

# Step 4: Eliminate the second variable (中錦) from the first and third rows
for i in [0, 2]:
    factor = matrix[i][1]
    matrix[i] = [matrix[i][j] - factor * matrix[1][j] for j in range(4)]

# Step 5: Normalize the third row by dividing by the third coefficient (new coefficient of 下錦)
factor = matrix[2][2]
matrix[2] = [Fraction(x, factor) for x in matrix[2]]

# Step 6: Eliminate the third variable (下錦) from the first and second rows
for i in [0, 1]:
    factor = matrix[i][2]
    matrix[i] = [matrix[i][j] - factor * matrix[2][j] for j in range(4)]

# The solution is now in the last column of the matrix
a = matrix[0][3]  # Value of 上錦 in terms of plain silk
b = matrix[1][3]  # Value of 中錦 in terms of plain silk
c = matrix[2][3]  # Value of 下錦 in terms of plain silk

# Output the results
a, b, c


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix.
2. **Row Operations**: The procedure systematically eliminates variables by normalizing rows and subtracting multiples of rows from others.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as required by the ancient procedure.
4. **Solution Extraction**: After elimination, the solution is found in the last column of the matrix.

### Answer:
The values of the silks in terms of plain silk are:
- 上錦 (upper silk): `a` plain silk
- 中錦 (middle silk): `b` plain silk
- 下錦 (lower silk): `c` plain silk
"""


"""
"""
