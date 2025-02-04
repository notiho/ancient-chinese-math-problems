"""
今有上禾二秉，中禾三秉，下禾四秉，實皆不滿斗。上取中，中取下，下取上各一秉而實滿斗。問︰上、中、下禾實一秉各幾何？
術曰：如方程，各置所取，以正負術入之。正負術曰：同名相除，異名相益，正無入負之，負無入正之。其異名相除，同名相益，正無入正之，負無入負之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉實 a斗 ，中禾一秉實 b斗 ，下禾一秉實 c斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code step by step, following the described method. The problem involves solving a system of linear equations using the described "正負術" (positive-negative method) and "方程術" (method of equations). Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given data:
# 上禾二秉，中禾三秉，下禾四秉
上禾秉數 = 2
中禾秉數 = 3
下禾秉數 = 4

# 實皆不滿斗
# 上取中，中取下，下取上各一秉而實滿斗
# This gives us the equations:
# 2a + b = 1
# 3b + c = 1
# 4c + a = 1

# Step 1: Represent the equations in matrix form
# Coefficients matrix:
# [2  1  0] [a]   [1]
# [0  3  1] [b] = [1]
# [1  0  4] [c]   [1]

# Step 2: Solve using elimination (方程術)

# Initialize variables
A = [[2, 1, 0],  # Coefficients of the first equation
     [0, 3, 1],  # Coefficients of the second equation
     [1, 0, 4]]  # Coefficients of the third equation
B = [1, 1, 1]    # Right-hand side values

# Elimination process
# Normalize the first row
factor = A[0][0]
A[0] = [Fraction(x, factor) for x in A[0]]
B[0] = Fraction(B[0], factor)

# Eliminate the first variable from the second and third rows
factor = A[1][0]
A[1] = [A[1][i] - factor * A[0][i] for i in range(3)]
B[1] = B[1] - factor * B[0]

factor = A[2][0]
A[2] = [A[2][i] - factor * A[0][i] for i in range(3)]
B[2] = B[2] - factor * B[0]

# Normalize the second row
factor = A[1][1]
A[1] = [Fraction(x, factor) for x in A[1]]
B[1] = Fraction(B[1], factor)

# Eliminate the second variable from the third row
factor = A[2][1]
A[2] = [A[2][i] - factor * A[1][i] for i in range(3)]
B[2] = B[2] - factor * B[1]

# Normalize the third row
factor = A[2][2]
A[2] = [Fraction(x, factor) for x in A[2]]
B[2] = Fraction(B[2], factor)

# Back substitution to find the values of a, b, c
c = B[2]
b = B[1] - A[1][2] * c
a = B[0] - A[0][1] * b - A[0][2] * c

# Results
a斗 = a
b斗 = b
c斗 = c

# Output the results
a斗, b斗, c斗
#----- content ends here -----


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented in matrix form, where `A` is the coefficient matrix and `B` is the right-hand side vector.
2. **Gaussian Elimination**: The elimination process is performed step by step to reduce the matrix to row-echelon form.
3. **Back Substitution**: Once the matrix is in row-echelon form, back substitution is used to solve for the variables `a`, `b`, and `c`.
4. **Fraction Handling**: The `Fraction` class is used to ensure precise calculations with fractions, as required by the problem.

### Final Answer:
The values of `a斗`, `b斗`, and `c斗` represent the amount of grain in one秉 for 上禾, 中禾, and 下禾, respectively.
"""


"""
"""
