"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem involves solving a system of linear equations to determine the prices of sheep, dogs, chickens, and rabbits. The ancient Chinese method described is equivalent to Gaussian elimination, which systematically reduces the equations to solve for the unknowns. Below is the Python implementation of the procedure:


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
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]

# Constants on the right-hand side
B = [1496, 1175, 958, 861]

# Step 1: Forward elimination
for i in range(len(A)):
    # Normalize the current row
    divisor = A[i][i]
    for j in range(len(A[i])):
        A[i][j] = Fraction(A[i][j], divisor)
    B[i] = Fraction(B[i], divisor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(A)):
        factor = A[k][i]
        for j in range(len(A[k])):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Step 2: Back substitution
x = [0] * len(A)
for i in range(len(A) - 1, -1, -1):
    x[i] = B[i]
    for j in range(i + 1, len(A)):
        x[i] -= A[i][j] * x[j]

# Results
a, b, c, d = x
print(f"羊價: {a}, 犬價: {b}, 雞價: {c}, 兔價: {d}")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the equations**: The coefficients of the variables (sheep, dogs, chickens, rabbits) and the constants on the right-hand side are stored in `A` and `B`, respectively.
2. **Forward elimination**: This step reduces the system of equations to an upper triangular form by normalizing each row and eliminating the variable from the rows below.
3. **Back substitution**: Starting from the last row, solve for each variable by substituting the already-solved variables into the equations.
4. **Output the results**: The prices of sheep, dogs, chickens, and rabbits are stored in `a`, `b`, `c`, and `d`, respectively.

### Answer:
The prices of sheep, dogs, chickens, and rabbits are:
- 羊價: `a`
- 犬價: `b`
- 雞價: `c`
- 兔價: `d`
"""


"""
"""
