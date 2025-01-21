"""
今有五羊四犬三雞二兔直錢一千四百九十六四羊二犬六雞三兔直錢一千一百七十五三羊一犬七雞五兔直錢九百五十八二羊三犬五雞一兔直錢八百六十一問羊犬雞兔價各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰羊價 a 犬價 b 雞價 c 兔價 d 
"""

"""
This problem is a classic system of linear equations problem, where the prices of sheep, dogs, chickens, and rabbits need to be determined based on the given relationships. The problem is solved using the ancient Chinese method of elimination, known as the "fangcheng" (方程) method, which is equivalent to Gaussian elimination in modern mathematics.

Here is the solution encoded in Python:


"""


from fractions import Fraction

# Given equations:
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Step 1: Represent the equations as a matrix
matrix = [
    [5, 4, 3, 2, 1496],  # Equation 1
    [4, 2, 6, 3, 1175],  # Equation 2
    [3, 1, 7, 5, 958],   # Equation 3
    [2, 3, 5, 1, 861]    # Equation 4
]

# Step 2: Perform Gaussian elimination (方程術)

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

# Step 3: Back substitution to find the values of 羊, 犬, 雞, and 兔

# Solve for 兔 (rabbit)
d = Fraction(matrix[3][4], matrix[3][3])

# Solve for 雞 (chicken)
c = Fraction(matrix[2][4] - matrix[2][3] * d, matrix[2][2])

# Solve for 犬 (dog)
b = Fraction(matrix[1][4] - matrix[1][2] * c - matrix[1][3] * d, matrix[1][1])

# Solve for 羊 (sheep)
a = Fraction(matrix[0][4] - matrix[0][1] * b - matrix[0][2] * c - matrix[0][3] * d, matrix[0][0])

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as a matrix where each row corresponds to one of the given equations.
2. **Gaussian Elimination**: The matrix is reduced step by step to an upper triangular form using the elimination method described in the "fangcheng" procedure.
3. **Back Substitution**: Once the matrix is in upper triangular form, the values of the variables (sheep, dog, chicken, rabbit prices) are calculated by back substitution.
4. **Fraction Class**: The `Fraction` class is used to ensure exact arithmetic, as required by the ancient Chinese method.

### Answer:
The prices of the animals are:
- 羊價 (sheep price): `a`
- 犬價 (dog price): `b`
- 雞價 (chicken price): `c`
- 兔價 (rabbit price): `d`
"""


"""
"""
