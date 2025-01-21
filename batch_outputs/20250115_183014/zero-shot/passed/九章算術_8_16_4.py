"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we will translate the given system of linear equations into Python code and compute the values of the unknowns \( a \), \( b \), \( c \), and \( d \), which represent the prices of sheep, dogs, chickens, and rabbits, respectively.

The equations are:
1. \( 5a + 4b + 3c + 2d = 1496 \)
2. \( 4a + 2b + 6c + 3d = 1175 \)
3. \( 3a + 1b + 7c + 5d = 958 \)
4. \( 2a + 3b + 5c + 1d = 861 \)

We will solve this system of equations using substitution or elimination.

Here is the Python code:


"""


from fractions import Fraction

# Define the equations as given
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a + 1b + 7c + 5d = 958
# 2a + 3b + 5c + 1d = 861

# Step 1: Solve for the unknowns using elimination
# We'll represent the equations in matrix form and solve step by step.

# Coefficients matrix
A = [
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]

# Constants on the right-hand side
B = [1496, 1175, 958, 861]

# Elimination process
# Make the first coefficient of the first row (A[0][0]) equal to 1
factor = Fraction(1, A[0][0])
A[0] = [factor * x for x in A[0]]
B[0] = factor * B[0]

# Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = A[i][0]
    A[i] = [A[i][j] - factor * A[0][j] for j in range(4)]
    B[i] = B[i] - factor * B[0]

# Make the second coefficient of the second row (A[1][1]) equal to 1
factor = Fraction(1, A[1][1])
A[1] = [factor * x for x in A[1]]
B[1] = factor * B[1]

# Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = A[i][1]
    A[i] = [A[i][j] - factor * A[1][j] for j in range(4)]
    B[i] = B[i] - factor * B[1]

# Make the third coefficient of the third row (A[2][2]) equal to 1
factor = Fraction(1, A[2][2])
A[2] = [factor * x for x in A[2]]
B[2] = factor * B[2]

# Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = A[i][2]
    A[i] = [A[i][j] - factor * A[2][j] for j in range(4)]
    B[i] = B[i] - factor * B[2]

# Make the fourth coefficient of the fourth row (A[3][3]) equal to 1
factor = Fraction(1, A[3][3])
A[3] = [factor * x for x in A[3]]
B[3] = factor * B[3]

# Eliminate the fourth variable from the other rows
for i in [0, 1, 2]:
    factor = A[i][3]
    A[i] = [A[i][j] - factor * A[3][j] for j in range(4)]
    B[i] = B[i] - factor * B[3]

# The solution is now in B
a = B[0]
b = B[1]
c = B[2]
d = B[3]

# Print the results
a, b, c, d


"""


This code uses the Gaussian elimination method to solve the system of linear equations. The results will be stored in the variables `a`, `b`, `c`, and `d`, which represent the prices of sheep, dogs, chickens, and rabbits, respectively.
"""


"""
"""
