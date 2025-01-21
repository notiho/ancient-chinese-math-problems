"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we need to translate the given system of equations into Python code and solve for the unknowns \( a \), \( b \), \( c \), and \( d \), which represent the prices of a sheep, a dog, a chicken, and a rabbit, respectively. We'll use the `Fraction` class to ensure precise calculations for non-integer results.

Here is the Python code:


"""


from fractions import Fraction

# Define the equations based on the problem statement
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a + 1b + 7c + 5d = 958
# 2a + 3b + 5c + 1d = 861

# Solve the system of equations using substitution or elimination
# Represent the equations in matrix form and solve step by step

# Coefficients matrix
A = [
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]

# Constants on the right-hand side
B = [1496, 1175, 958, 861]

# Step 1: Eliminate variables to solve for one at a time
# Convert A and B into fractions for precise calculations
A = [[Fraction(x) for x in row] for row in A]
B = [Fraction(x) for x in B]

# Gaussian elimination
for i in range(4):
    # Make the diagonal element 1
    diag = A[i][i]
    for j in range(i, 4):
        A[i][j] /= diag
    B[i] /= diag
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, 4):
        factor = A[k][i]
        for j in range(i, 4):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Back substitution to find the values of a, b, c, d
d = B[3]
c = B[2] - A[2][3] * d
b = B[1] - A[1][2] * c - A[1][3] * d
a = B[0] - A[0][1] * b - A[0][2] * c - A[0][3] * d

# The solutions
a, b, c, d


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented in matrix form \( A \cdot X = B \), where \( A \) is the coefficients matrix, \( X \) is the vector of unknowns \([a, b, c, d]\), and \( B \) is the constants vector.
2. **Gaussian Elimination**: The system is solved using Gaussian elimination, which involves:
   - Making the diagonal elements of the matrix \( A \) equal to 1.
   - Eliminating variables row by row to simplify the system.
3. **Back Substitution**: After elimination, the values of \( a \), \( b \), \( c \), and \( d \) are computed by substituting known values into the equations.

### Final Values:
After running the code, the values of \( a \), \( b \), \( c \), and \( d \) will be stored in the respective variables. These represent the prices of a sheep, a dog, a chicken, and a rabbit, respectively.
"""


"""
"""
