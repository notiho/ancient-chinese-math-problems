"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：武馬一匹力引 a石 ，中馬一匹力引 b石 ，下馬一匹力引 c石 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step. The problem involves solving a system of linear equations using the described method, which is equivalent to Gaussian elimination. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the coefficients of the equations
# 武馬 (x), 中馬 (y), 下馬 (z)
# The equations are derived from the problem:
# x + y = 40
# y + z = 40
# z + x = 40

# Coefficients matrix (augmented matrix)
matrix = [
    [1, 1, 0, 40],  # x + y = 40
    [0, 1, 1, 40],  # y + z = 40
    [1, 0, 1, 40]   # z + x = 40
]

# Step 2: Perform Gaussian elimination
# Normalize the first row
factor = matrix[0][0]
for j in range(4):
    matrix[0][j] = Fraction(matrix[0][j], factor)

# Eliminate the first variable (x) from the second and third rows
for i in range(1, 3):
    factor = matrix[i][0]
    for j in range(4):
        matrix[i][j] -= factor * matrix[0][j]

# Normalize the second row
factor = matrix[1][1]
for j in range(1, 4):
    matrix[1][j] = Fraction(matrix[1][j], factor)

# Eliminate the second variable (y) from the third row
factor = matrix[2][1]
for j in range(1, 4):
    matrix[2][j] -= factor * matrix[1][j]

# Normalize the third row
factor = matrix[2][2]
matrix[2][3] = Fraction(matrix[2][3], factor)

# Step 3: Back substitution to solve for x, y, z
z = matrix[2][3]
y = matrix[1][3] - matrix[1][2] * z
x = matrix[0][3] - matrix[0][1] * y - matrix[0][2] * z

# Results
a = x  # 武馬力引
b = y  # 中馬力引
c = z  # 下馬力引

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as a system of linear equations, and the coefficients are stored in an augmented matrix.
2. **Gaussian Elimination**: The procedure described in the ancient text is equivalent to Gaussian elimination. We normalize rows and eliminate variables step by step.
3. **Back Substitution**: After the matrix is in row-echelon form, we solve for the variables (武馬, 中馬, 下馬) using back substitution.
4. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic, as required by the problem.

### Final Answer:
The values of `a`, `b`, and `c` represent the pulling forces of 武馬, 中馬, and 下馬, respectively, in terms of 石 (shi).
"""


"""
Variable 'a' has wrong value. Expected: 160/7, Actual: 20
Variable 'b' has wrong value. Expected: 120/7, Actual: 20
Variable 'c' has wrong value. Expected: 40/7, Actual: 20"""
