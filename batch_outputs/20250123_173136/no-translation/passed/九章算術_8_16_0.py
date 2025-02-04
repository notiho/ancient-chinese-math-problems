"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem involves solving a system of linear equations, which is a classic example of ancient Chinese mathematics using the "正負術" (method of elimination). Below is the Python code to solve the problem step by step:


"""


from fractions import Fraction

# Coefficients of the equations
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Step 1: Represent the equations as a matrix
matrix = [
    [5, 4, 3, 2, 1496],
    [4, 2, 6, 3, 1175],
    [3, 1, 7, 5, 958],
    [2, 3, 5, 1, 861]
]

# Step 2: Perform Gaussian elimination
# Normalize the first row
for i in range(1, 4):
    factor = Fraction(matrix[i][0], matrix[0][0])
    for j in range(5):
        matrix[i][j] -= factor * matrix[0][j]

# Normalize the second row
for i in range(2, 4):
    factor = Fraction(matrix[i][1], matrix[1][1])
    for j in range(1, 5):
        matrix[i][j] -= factor * matrix[1][j]

# Normalize the third row
factor = Fraction(matrix[3][2], matrix[2][2])
for j in range(2, 5):
    matrix[3][j] -= factor * matrix[2][j]

# Step 3: Back substitution
d = Fraction(matrix[3][4], matrix[3][3])
c = Fraction(matrix[2][4] - matrix[2][3] * d, matrix[2][2])
b = Fraction(matrix[1][4] - matrix[1][2] * c - matrix[1][3] * d, matrix[1][1])
a = Fraction(matrix[0][4] - matrix[0][1] * b - matrix[0][2] * c - matrix[0][3] * d, matrix[0][0])

# Results
a = float(a)  # 羊價
b = float(b)  # 犬價
c = float(c)  # 雞價
d = float(d)  # 兔價

print(f"羊價 a = {a}, 犬價 b = {b}, 雞價 c = {c}, 兔價 d = {d}")


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented as a matrix where each row corresponds to an equation, and the last column represents the constants on the right-hand side of the equations.
2. **Gaussian Elimination**: The matrix is reduced to row-echelon form using the method of elimination described in the problem. This involves subtracting multiples of one row from another to eliminate variables step by step.
3. **Back Substitution**: Once the matrix is in row-echelon form, the values of the variables are determined by substituting back from the bottom row to the top.
4. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.

### Final Answer:
The values of `a`, `b`, `c`, and `d` represent the prices of the sheep, dog, chicken, and rabbit, respectively.
"""


"""
"""
