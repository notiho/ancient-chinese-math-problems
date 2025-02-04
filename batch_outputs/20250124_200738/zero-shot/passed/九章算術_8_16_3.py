"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we need to translate the ancient Chinese mathematical problem into a system of linear equations and solve for the unknowns \(a\), \(b\), \(c\), and \(d\), which represent the prices of sheep, dogs, chickens, and rabbits, respectively. Here's the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem statement:
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a + 1b + 7c + 5d = 958
# 2a + 3b + 5c + 1d = 861

# Solve the system of equations using substitution or elimination.

# Step 1: Represent the equations in matrix form
# Coefficients matrix
A = [
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]

# Constants on the right-hand side
B = [1496, 1175, 958, 861]

# Step 2: Use Gaussian elimination to solve for a, b, c, d

# Convert A and B into fractions for exact arithmetic
A = [[Fraction(num) for num in row] for row in A]
B = [Fraction(num) for num in B]

# Forward elimination
for i in range(4):
    # Make the diagonal element 1 by dividing the row
    diag = A[i][i]
    for j in range(4):
        A[i][j] /= diag
    B[i] /= diag

    # Eliminate the current column in the rows below
    for k in range(i + 1, 4):
        factor = A[k][i]
        for j in range(4):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Back substitution
x = [0, 0, 0, 0]  # To store the solutions
for i in range(3, -1, -1):
    x[i] = B[i]
    for j in range(i + 1, 4):
        x[i] -= A[i][j] * x[j]

# Assign the solutions to the variables
a = x[0]
b = x[1]
c = x[2]
d = x[3]

# Print the results
a, b, c, d
#----- content ends here -----


"""


### Explanation:
1. The problem is represented as a system of linear equations.
2. Gaussian elimination is used to solve the system step by step:
   - Forward elimination makes the matrix upper triangular.
   - Back substitution solves for the unknowns.
3. The `Fraction` class ensures exact arithmetic for non-integer results.

### Solution:
After running the code, the variables `a`, `b`, `c`, and `d` will contain the exact prices of the sheep, dogs, chickens, and rabbits, respectively.
"""


"""
"""
