"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a(=177) ，犬價 b(=121) ，雞價 c(=23) ，兔價 d(=29) 。
"""

"""
The problem involves solving a system of linear equations to determine the prices of sheep, dogs, chickens, and rabbits. The ancient Chinese method described here is equivalent to solving simultaneous linear equations using elimination (similar to Gaussian elimination). Below is the Python implementation of the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given equations:
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Coefficients of the equations
A = [
    [5, 4, 3, 2],  # Coefficients of the first equation
    [4, 2, 6, 3],  # Coefficients of the second equation
    [3, 1, 7, 5],  # Coefficients of the third equation
    [2, 3, 5, 1],  # Coefficients of the fourth equation
]

# Constants on the right-hand side
B = [1496, 1175, 958, 861]

# Step 1: Convert to fractions for exact arithmetic
A = [[Fraction(x) for x in row] for row in A]
B = [Fraction(x) for x in B]

# Step 2: Perform Gaussian elimination
n = len(A)

for i in range(n):
    # Make the diagonal element 1 by dividing the row
    diag = A[i][i]
    for j in range(i, n):
        A[i][j] /= diag
    B[i] /= diag

    # Eliminate the current variable from the rows below
    for k in range(i + 1, n):
        factor = A[k][i]
        for j in range(i, n):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Step 3: Back substitution to solve for variables
X = [0] * n
for i in range(n - 1, -1, -1):
    X[i] = B[i]
    for j in range(i + 1, n):
        X[i] -= A[i][j] * X[j]

# Results
a, b, c, d = X  # Prices of sheep, dogs, chickens, and rabbits
print(f"羊價 a = {a}, 犬價 b = {b}, 雞價 c = {c}, 兔價 d = {d}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the equations**: The coefficients of the variables (sheep, dogs, chickens, rabbits) and the constants on the right-hand side are stored in `A` and `B`.
2. **Fractions for exact arithmetic**: The `Fraction` class is used to ensure exact calculations without floating-point errors.
3. **Gaussian elimination**: The system of equations is solved by eliminating variables row by row, making the matrix upper triangular.
4. **Back substitution**: The solution is obtained by substituting values from the bottom row upwards.
5. **Output**: The prices of sheep (`a`), dogs (`b`), chickens (`c`), and rabbits (`d`) are printed.

### Answer:
```
羊價 a = 177, 犬價 b = 121, 雞價 c = 23, 兔價 d = 29
```
"""


"""
"""
