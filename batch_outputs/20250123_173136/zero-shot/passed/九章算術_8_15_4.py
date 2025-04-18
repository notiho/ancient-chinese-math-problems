"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：令一人食 a雞 ，吏一人食 b雞 ，從者一人食 c雞 。
"""

"""
To solve the problem, we will translate the ancient Chinese mathematical problem into a system of linear equations and solve for the unknowns \(a\), \(b\), and \(c\), which represent the number of chickens eaten by a single "令" (official), "吏" (clerk), and "從者" (attendant), respectively.

The problem gives us the following equations based on the number of people and the total chickens consumed:

1. \(1a + 5b + 10c = 10\)
2. \(10a + 1b + 5c = 8\)
3. \(5a + 10b + 1c = 6\)

We will solve this system of equations using Python and the `Fraction` class for precise arithmetic.


"""


from fractions import Fraction

# Coefficients of the equations
# 1a + 5b + 10c = 10
# 10a + 1b + 5c = 8
# 5a + 10b + 1c = 6

# Step 1: Represent the equations as a matrix
# Equation 1: a + 5b + 10c = 10
# Equation 2: 10a + b + 5c = 8
# Equation 3: 5a + 10b + c = 6

# Using elimination to solve for a, b, and c
# Convert to fractions for precise arithmetic
A = [
    [Fraction(1), Fraction(5), Fraction(10)],  # Coefficients of equation 1
    [Fraction(10), Fraction(1), Fraction(5)],  # Coefficients of equation 2
    [Fraction(5), Fraction(10), Fraction(1)]   # Coefficients of equation 3
]
B = [Fraction(10), Fraction(8), Fraction(6)]  # Right-hand side of the equations

# Step 2: Eliminate variables to solve
# Forward elimination
# Make the first coefficient of the first row 1 (already 1 in this case)
for i in range(3):
    # Normalize the current row
    factor = A[i][i]
    for j in range(3):
        A[i][j] /= factor
    B[i] /= factor

    # Eliminate the current variable from the rows below
    for k in range(i + 1, 3):
        factor = A[k][i]
        for j in range(3):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Back substitution
c = B[2] / A[2][2]
b = (B[1] - A[1][2] * c) / A[1][1]
a = (B[0] - A[0][1] * b - A[0][2] * c) / A[0][0]

# The solutions
a, b, c


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix \(A\) for the coefficients and a vector \(B\) for the constants on the right-hand side.
2. **Forward Elimination**: The matrix is transformed into an upper triangular form by eliminating variables row by row.
3. **Back Substitution**: Starting from the last row, the values of \(c\), \(b\), and \(a\) are computed sequentially.

### Solution:
The values of \(a\), \(b\), and \(c\) will be computed as fractions, ensuring precise results.
"""


"""
"""
