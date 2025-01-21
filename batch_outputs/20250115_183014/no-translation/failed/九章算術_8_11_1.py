"""
今有武馬一匹，中馬二匹，下馬三匹，皆載四十石至阪，皆不能上。武馬借中馬一匹，中馬借下馬一匹，下馬借武馬一匹，乃皆上。問︰武、中、下馬一匹各力引幾何？
術曰：如方程各置所借，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：武馬 a匹 力引 b石 ，中馬 c匹 力引 d石 ，下馬 e匹 力引 f石 。
"""

"""
To solve this problem, we need to translate the ancient Chinese mathematical procedure into Python code. The problem involves solving a system of linear equations using the described method. Here's the Python implementation:


"""


from fractions import Fraction

# Define the coefficients of the equations based on the problem
# 武馬 (x), 中馬 (y), 下馬 (z)
# Equation 1: 武馬 + 中馬 + 下馬 = 40石
# Equation 2: 武馬借中馬 (武馬 + 中馬) = 40石
# Equation 3: 中馬借下馬 (中馬 + 下馬) = 40石
# Equation 4: 下馬借武馬 (下馬 + 武馬) = 40石

# Coefficients matrix (augmented matrix)
# Each row represents an equation: [武馬, 中馬, 下馬, constant]
matrix = [
    [1, 1, 1, 40],  # 武馬 + 中馬 + 下馬 = 40
    [1, 1, 0, 40],  # 武馬 + 中馬 = 40
    [0, 1, 1, 40],  # 中馬 + 下馬 = 40
    [1, 0, 1, 40]   # 下馬 + 武馬 = 40
]

# Gaussian elimination to solve the system of equations
# Step 1: Normalize the first row
for i in range(4):
    matrix[0][i] = Fraction(matrix[0][i], matrix[0][0])

# Step 2: Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = matrix[i][0]
    for j in range(4):
        matrix[i][j] -= factor * matrix[0][j]

# Step 3: Normalize the second row
for i in range(1, 4):
    matrix[1][i] = Fraction(matrix[1][i], matrix[1][1])

# Step 4: Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = matrix[i][1]
    for j in range(1, 4):
        matrix[i][j] -= factor * matrix[1][j]

# Step 5: Normalize the third row
for i in range(2, 4):
    matrix[2][i] = Fraction(matrix[2][i], matrix[2][2])

# Step 6: Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = matrix[i][2]
    for j in range(2, 4):
        matrix[i][j] -= factor * matrix[2][j]

# Step 7: Normalize the fourth row
matrix[3][3] = Fraction(matrix[3][3], matrix[3][3])

# Extract the solutions
武馬 = matrix[0][3]
中馬 = matrix[1][3]
下馬 = matrix[2][3]

# Output the results
a = 1  # 武馬 1匹
b = 武馬  # 武馬力引 b石
c = 1  # 中馬 1匹
d = 中馬  # 中馬力引 d石
e = 1  # 下馬 1匹
f = 下馬  # 下馬力引 f石

print(f"武馬 {a}匹 力引 {b}石")
print(f"中馬 {c}匹 力引 {d}石")
print(f"下馬 {e}匹 力引 {f}石")


"""


This code implements the described procedure using Gaussian elimination to solve the system of linear equations. The results for `武馬`, `中馬`, and `下馬` are calculated as fractions to ensure accuracy.
"""


"""
Code error: Fraction(0, 0)"""
