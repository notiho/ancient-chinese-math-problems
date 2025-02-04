"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem is a classic system of linear equations, where we solve for the prices of sheep (羊), dogs (犬), chickens (雞), and rabbits (兔). The solution involves applying the method of elimination, as described in the ancient Chinese "方程術" (method of solving simultaneous equations). Below is the Python implementation of the solution:


"""


from fractions import Fraction

# Given equations:
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Coefficients of the equations
A = [
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]

# Constants (right-hand side of the equations)
B = [1496, 1175, 958, 861]

# Step 1: Eliminate variables to form an upper triangular matrix
for i in range(len(A)):
    # Normalize the current row
    factor = A[i][i]
    for j in range(i, len(A[i])):
        A[i][j] = Fraction(A[i][j], factor)
    B[i] = Fraction(B[i], factor)
    
    # Eliminate the current variable from subsequent rows
    for k in range(i + 1, len(A)):
        factor = A[k][i]
        for j in range(i, len(A[k])):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Step 2: Back substitution to solve for the variables
n = len(A)
X = [0] * n
for i in range(n - 1, -1, -1):
    X[i] = B[i]
    for j in range(i + 1, n):
        X[i] -= A[i][j] * X[j]

# Assign the results to the respective variables
a = X[0]  # 羊價
b = X[1]  # 犬價
c = X[2]  # 雞價
d = X[3]  # 兔價

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Input the equations**: The coefficients of the variables (羊, 犬, 雞, 兔) are stored in matrix `A`, and the constants on the right-hand side are stored in list `B`.
2. **Gaussian elimination**: The first loop normalizes each row and eliminates the variable from subsequent rows to form an upper triangular matrix.
3. **Back substitution**: Starting from the last row, solve for each variable by substituting the known values back into the equations.
4. **Output**: The values of `a`, `b`, `c`, and `d` represent the prices of sheep, dogs, chickens, and rabbits, respectively.

### Answer:
The prices are:
- 羊價 `a`
- 犬價 `b`
- 雞價 `c`
- 兔價 `d`

You can run the code to compute the exact values of `a`, `b`, `c`, and `d` as fractions or decimals.
"""


"""
"""
