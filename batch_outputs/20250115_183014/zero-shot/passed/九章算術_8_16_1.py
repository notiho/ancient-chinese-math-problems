"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into a system of linear equations and solve for the unknowns \( a \), \( b \), \( c \), and \( d \), which represent the prices of a sheep, a dog, a chicken, and a rabbit, respectively.

The equations are derived from the problem statement:

1. \( 5a + 4b + 3c + 2d = 1496 \)
2. \( 4a + 2b + 6c + 3d = 1175 \)
3. \( 3a + b + 7c + 5d = 958 \)
4. \( 2a + 3b + 5c + d = 861 \)

We will solve this system of equations using Python code. Here's the implementation:


"""


from fractions import Fraction

# Define the coefficients of the equations
# 5a + 4b + 3c + 2d = 1496
# 4a + 2b + 6c + 3d = 1175
# 3a + 1b + 7c + 5d = 958
# 2a + 3b + 5c + 1d = 861

# Solve the system of equations using substitution/elimination
# Representing the equations in matrix form:
# | 5  4  3  2 |   | a |   =   | 1496 |
# | 4  2  6  3 | * | b |   =   | 1175 |
# | 3  1  7  5 |   | c |   =   |  958 |
# | 2  3  5  1 |   | d |   =   |  861 |

# Step 1: Eliminate 'a' from equations 2, 3, and 4
# Multiply row 1 by appropriate factors and subtract from other rows
row1 = [5, 4, 3, 2, 1496]
row2 = [4, 2, 6, 3, 1175]
row3 = [3, 1, 7, 5, 958]
row4 = [2, 3, 5, 1, 861]

# Normalize row 1 by dividing by 5
row1 = [Fraction(x, 5) for x in row1]

# Eliminate 'a' from row 2
factor = row2[0]
row2 = [row2[i] - factor * row1[i] for i in range(5)]

# Eliminate 'a' from row 3
factor = row3[0]
row3 = [row3[i] - factor * row1[i] for i in range(5)]

# Eliminate 'a' from row 4
factor = row4[0]
row4 = [row4[i] - factor * row1[i] for i in range(5)]

# Step 2: Eliminate 'b' from equations 3 and 4
# Normalize row 2 by dividing by its second element
row2 = [Fraction(x, row2[1]) for x in row2]

# Eliminate 'b' from row 3
factor = row3[1]
row3 = [row3[i] - factor * row2[i] for i in range(5)]

# Eliminate 'b' from row 4
factor = row4[1]
row4 = [row4[i] - factor * row2[i] for i in range(5)]

# Step 3: Eliminate 'c' from equation 4
# Normalize row 3 by dividing by its third element
row3 = [Fraction(x, row3[2]) for x in row3]

# Eliminate 'c' from row 4
factor = row4[2]
row4 = [row4[i] - factor * row3[i] for i in range(5)]

# Step 4: Back-substitution to solve for d, c, b, and a
d = row4[4] / row4[3]
c = row3[4] - row3[3] * d
b = row2[4] - row2[3] * d - row2[2] * c
a = row1[4] - row1[3] * d - row1[2] * c - row1[1] * b

# The results
a = float(a)
b = float(b)
c = float(c)
d = float(d)

print(f"a (sheep price): {a}")
print(f"b (dog price): {b}")
print(f"c (chicken price): {c}")
print(f"d (rabbit price): {d}")


"""


This code solves the system of equations using Gaussian elimination. The results for \( a \), \( b \), \( c \), and \( d \) will be printed as the prices of the sheep, dog, chicken, and rabbit, respectively.
"""


"""
"""
