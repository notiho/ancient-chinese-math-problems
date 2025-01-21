"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem is a system of linear equations, and the solution involves solving for the values of the variables (prices of sheep, dogs, chickens, and rabbits). Below is the Python implementation of the described procedure using the "正負術" (Gaussian elimination-like method):


"""


from fractions import Fraction

# Coefficients of the equations
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Initialize the augmented matrix
matrix = [
    [5, 4, 3, 2, 1496],
    [4, 2, 6, 3, 1175],
    [3, 1, 7, 5, 958],
    [2, 3, 5, 1, 861]
]

# Step 1: Normalize the first row
for i in range(5):
    matrix[0][i] = Fraction(matrix[0][i], matrix[0][0])

# Step 2: Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = matrix[i][0]
    for j in range(5):
        matrix[i][j] -= factor * matrix[0][j]

# Step 3: Normalize the second row
for i in range(1, 5):
    matrix[1][i] = Fraction(matrix[1][i], matrix[1][1])

# Step 4: Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = matrix[i][1]
    for j in range(1, 5):
        matrix[i][j] -= factor * matrix[1][j]

# Step 5: Normalize the third row
for i in range(2, 5):
    matrix[2][i] = Fraction(matrix[2][i], matrix[2][2])

# Step 6: Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = matrix[i][2]
    for j in range(2, 5):
        matrix[i][j] -= factor * matrix[2][j]

# Step 7: Normalize the fourth row
for i in range(3, 5):
    matrix[3][i] = Fraction(matrix[3][i], matrix[3][3])

# Step 8: Back-substitute to find the values of the variables
d = matrix[3][4]
c = matrix[2][4] - matrix[2][3] * d
b = matrix[1][4] - matrix[1][2] * c - matrix[1][3] * d
a = matrix[0][4] - matrix[0][1] * b - matrix[0][2] * c - matrix[0][3] * d

# Results
a = float(a)
b = float(b)
c = float(c)
d = float(d)

print(f"羊價 a = {a}")
print(f"犬價 b = {b}")
print(f"雞價 c = {c}")
print(f"兔價 d = {d}")


"""


This code follows the procedure described in the problem, using Gaussian elimination to solve the system of linear equations. The results (`a`, `b`, `c`, `d`) represent the prices of sheep, dogs, chickens, and rabbits, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 177, Actual: 2725122965.0
Variable 'b' has wrong value. Expected: 121, Actual: -605780358.0
Variable 'c' has wrong value. Expected: 23, Actual: -99483029.0
Variable 'd' has wrong value. Expected: 29, Actual: -1775475.0"""
