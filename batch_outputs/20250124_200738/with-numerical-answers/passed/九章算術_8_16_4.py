"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a(=177) ，犬價 b(=121) ，雞價 c(=23) ，兔價 d(=29) 。
"""

"""
The problem involves solving a system of linear equations to determine the prices of sheep, dogs, chickens, and rabbits. The ancient Chinese method described here is equivalent to solving the system using Gaussian elimination. Below is the Python implementation of the procedure:


"""

#----- content starts here -----

from fractions import Fraction

# Equations:
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Coefficients of the equations
matrix = [
    [5, 4, 3, 2, 1496],
    [4, 2, 6, 3, 1175],
    [3, 1, 7, 5, 958],
    [2, 3, 5, 1, 861]
]

# Step 1: Normalize the first row
for i in range(1, 4):
    factor = Fraction(matrix[i][0], matrix[0][0])
    for j in range(5):
        matrix[i][j] -= factor * matrix[0][j]

# Step 2: Normalize the second row
for i in range(2, 4):
    factor = Fraction(matrix[i][1], matrix[1][1])
    for j in range(1, 5):
        matrix[i][j] -= factor * matrix[1][j]

# Step 3: Normalize the third row
factor = Fraction(matrix[3][2], matrix[2][2])
for j in range(2, 5):
    matrix[3][j] -= factor * matrix[2][j]

# Step 4: Back substitution to solve for variables
d = Fraction(matrix[3][4], matrix[3][3])
c = Fraction(matrix[2][4] - matrix[2][3] * d, matrix[2][2])
b = Fraction(matrix[1][4] - matrix[1][2] * c - matrix[1][3] * d, matrix[1][1])
a = Fraction(matrix[0][4] - matrix[0][1] * b - matrix[0][2] * c - matrix[0][3] * d, matrix[0][0])

# Results
a = int(a)  # 羊價
b = int(b)  # 犬價
c = int(c)  # 雞價
d = int(d)  # 兔價

print(f"羊價 a={a} ，犬價 b={b} ，雞價 c={c} ，兔價 d={d} 。")
#----- content ends here -----


"""


### Explanation:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix.
2. **Gaussian Elimination**: The matrix is reduced row by row to simplify the equations, eliminating variables step by step.
3. **Back Substitution**: Once the matrix is in row-echelon form, the variables are solved starting from the last equation.

### Answer:
```
羊價 a=177 ，犬價 b=121 ，雞價 c=23 ，兔價 d=29 。
```
"""


"""
"""
