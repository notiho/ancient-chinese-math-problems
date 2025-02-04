"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we will translate the given system of linear equations into Python code and compute the values of the unknowns \( a \), \( b \), \( c \), and \( d \) using the class `Fraction` to ensure precise calculations. Here's the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem statement
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a + 1b + 7c + 5d = 958
# 2a + 3b + 5c + 1d = 861

# Solve the system of equations using substitution or elimination

# Step 1: Represent the equations in matrix form
# Coefficients matrix
A = [
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]

# Constants vector
B = [1496, 1175, 958, 861]

# Step 2: Use Gaussian elimination to solve for a, b, c, d
# Convert A and B into fractions for precise calculations
A = [[Fraction(num) for num in row] for row in A]
B = [Fraction(num) for num in B]

# Forward elimination
for i in range(4):
    # Make the diagonal element 1
    diag = A[i][i]
    for j in range(i, 4):
        A[i][j] /= diag
    B[i] /= diag

    # Eliminate the current column in rows below
    for k in range(i + 1, 4):
        factor = A[k][i]
        for j in range(i, 4):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Back substitution
x = [Fraction(0) for _ in range(4)]
for i in range(3, -1, -1):
    x[i] = B[i]
    for j in range(i + 1, 4):
        x[i] -= A[i][j] * x[j]

# Assign the solutions to the variables
a, b, c, d = x

# Print the results
a, b, c, d


"""


### Explanation of the Code:
1. **Matrix Representation**: The coefficients of the unknowns \( a, b, c, d \) are stored in a matrix `A`, and the constants on the right-hand side of the equations are stored in a vector `B`.

2. **Gaussian Elimination**:
   - **Forward Elimination**: The matrix is transformed into an upper triangular form by eliminating the lower elements of each column.
   - **Back Substitution**: The values of the unknowns are computed starting from the last row and substituting back into the previous rows.

3. **Fraction Class**: The `Fraction` class is used to ensure that all calculations are precise and avoid rounding errors.

### Output:
The variables `a`, `b`, `c`, and `d` will contain the prices of the sheep, dog, chicken, and rabbit, respectively, in terms of fractions or integers.
"""


"""
"""
