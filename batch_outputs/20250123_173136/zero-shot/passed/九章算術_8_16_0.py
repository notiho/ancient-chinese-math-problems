"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we will translate the given system of linear equations into Python code. The problem involves four unknowns: the prices of a sheep (`a`), a dog (`b`), a chicken (`c`), and a rabbit (`d`). The equations are as follows:

1. \( 5a + 4b + 3c + 2d = 1496 \)
2. \( 4a + 2b + 6c + 3d = 1175 \)
3. \( 3a + 1b + 7c + 5d = 958 \)
4. \( 2a + 3b + 5c + 1d = 861 \)

We will solve this system of equations using Python and the `Fraction` class to ensure exact arithmetic.

Here is the Python code:


"""


from fractions import Fraction

# Define the coefficients of the equations
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a + 1b + 7c + 5d = 958
# 2a + 3b + 5c + 1d = 861

# Coefficients matrix
A = [
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]

# Constants on the right-hand side
B = [1496, 1175, 958, 861]

# Convert all numbers to Fractions for exact arithmetic
A = [[Fraction(num) for num in row] for row in A]
B = [Fraction(num) for num in B]

# Gaussian elimination
n = len(A)

# Forward elimination
for i in range(n):
    # Make the diagonal element 1
    diag_factor = A[i][i]
    for j in range(i, n):
        A[i][j] /= diag_factor
    B[i] /= diag_factor

    # Make the elements below the diagonal 0
    for k in range(i + 1, n):
        factor = A[k][i]
        for j in range(i, n):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Back substitution
x = [Fraction(0) for _ in range(n)]
for i in range(n - 1, -1, -1):
    x[i] = B[i]
    for j in range(i + 1, n):
        x[i] -= A[i][j] * x[j]

# Assign the solutions to variables
a, b, c, d = x

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. The coefficients of the equations are stored in matrix `A`, and the constants on the right-hand side are stored in vector `B`.
2. All numbers are converted to `Fraction` to ensure exact arithmetic.
3. Gaussian elimination is used to solve the system of linear equations:
   - In the forward elimination step, the matrix is transformed into an upper triangular form.
   - In the back substitution step, the solutions are computed.
4. The solutions are assigned to the variables `a`, `b`, `c`, and `d`.

### Output:
The values of `a`, `b`, `c`, and `d` will be the prices of a sheep, a dog, a chicken, and a rabbit, respectively.
"""


"""
"""
