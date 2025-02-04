"""
今有五羊、四犬、三雞、二兔，直錢一千四百九十六；四羊、二犬、六雞、三兔直錢一千一百七十五；三羊、一犬、七雞、五兔，直錢九百五十八；二羊、三犬、五雞、一兔，直錢八百六十一。問︰羊、犬、雞、兔價各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：羊價 a ，犬價 b ，雞價 c ，兔價 d 。
"""

"""
This problem involves solving a system of linear equations, which is described in the ancient Chinese mathematical text as "方程術" (method of solving simultaneous equations). Below is the Python implementation of the described procedure using the Fraction class to ensure precise calculations.


"""


from fractions import Fraction

# Coefficients of the equations
# 5羊 + 4犬 + 3雞 + 2兔 = 1496
# 4羊 + 2犬 + 6雞 + 3兔 = 1175
# 3羊 + 1犬 + 7雞 + 5兔 = 958
# 2羊 + 3犬 + 5雞 + 1兔 = 861

# Define the coefficients and constants
coefficients = [
    [5, 4, 3, 2],
    [4, 2, 6, 3],
    [3, 1, 7, 5],
    [2, 3, 5, 1]
]
constants = [1496, 1175, 958, 861]

# Step 1: Convert the coefficients and constants into fractions
for i in range(len(coefficients)):
    coefficients[i] = [Fraction(x) for x in coefficients[i]]
constants = [Fraction(x) for x in constants]

# Step 2: Gaussian elimination
n = len(coefficients)

# Forward elimination
for i in range(n):
    # Make the diagonal element 1 by dividing the row
    diag = coefficients[i][i]
    for j in range(i, n):
        coefficients[i][j] /= diag
    constants[i] /= diag

    # Eliminate the current variable from the rows below
    for k in range(i + 1, n):
        factor = coefficients[k][i]
        for j in range(i, n):
            coefficients[k][j] -= factor * coefficients[i][j]
        constants[k] -= factor * constants[i]

# Back substitution
solution = [0] * n
for i in range(n - 1, -1, -1):
    solution[i] = constants[i]
    for j in range(i + 1, n):
        solution[i] -= coefficients[i][j] * solution[j]

# Assign the solutions to variables
a = solution[0]  # 羊價
b = solution[1]  # 犬價
c = solution[2]  # 雞價
d = solution[3]  # 兔價

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. **Input Representation**: The coefficients of the equations and the constants are represented as lists. Each coefficient is converted to a `Fraction` to ensure precise arithmetic.
2. **Gaussian Elimination**:
   - **Forward Elimination**: The matrix is transformed into an upper triangular form by making the diagonal elements 1 and eliminating the variables from the rows below.
   - **Back Substitution**: Starting from the last row, the values of the variables are calculated by substituting the known values into the equations.
3. **Output**: The values of `a`, `b`, `c`, and `d` represent the prices of the sheep, dog, chicken, and rabbit, respectively.

This implementation follows the ancient procedure described in the problem, ensuring that the solution is derived step by step using the "正負術" (positive-negative method).
"""


"""
"""
