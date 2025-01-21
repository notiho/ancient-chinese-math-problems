"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：麻 a斗 b錢 ，麥 c斗 d錢 ，菽 e斗 f錢 ，答 g斗 h錢 ，黍 i斗 j錢 。
"""

"""
To solve this problem, we need to translate the ancient Chinese system of equations into Python code and compute the values of the unknowns. The unknowns are the prices per unit (斗) of 麻 (a), 麥 (c), 菽 (e), 答 (g), and 黍 (i). We'll use the `Fraction` class to handle non-integer results.

Here is the Python code:


"""


from fractions import Fraction

# Define the system of equations based on the problem statement
# Each equation represents the total price (in 錢) for a given combination of 麻, 麥, 菽, 答, and 黍
# 麻 = a, 麥 = c, 菽 = e, 答 = g, 黍 = i
# The equations are:
# 9a + 7c + 3e + 2g + 5i = 140
# 7a + 6c + 4e + 5g + 3i = 128
# 3a + 5c + 7e + 6g + 4i = 116
# 2a + 5c + 3e + 9g + 4i = 112
# 1a + 3c + 2e + 8g + 5i = 95

# Solve the system of equations using substitution or elimination
# We'll represent the equations in matrix form and solve step by step

# Coefficients matrix
A = [
    [9, 7, 3, 2, 5],
    [7, 6, 4, 5, 3],
    [3, 5, 7, 6, 4],
    [2, 5, 3, 9, 4],
    [1, 3, 2, 8, 5]
]

# Constants (right-hand side)
B = [140, 128, 116, 112, 95]

# Convert to fractions for precise calculations
A = [[Fraction(x) for x in row] for row in A]
B = [Fraction(x) for x in B]

# Gaussian elimination
for i in range(len(A)):
    # Make the diagonal element 1
    diag = A[i][i]
    for j in range(len(A[i])):
        A[i][j] /= diag
    B[i] /= diag

    # Eliminate the current column in rows below
    for k in range(i + 1, len(A)):
        factor = A[k][i]
        for j in range(len(A[k])):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Back substitution
x = [0] * len(B)
for i in range(len(A) - 1, -1, -1):
    x[i] = B[i]
    for j in range(i + 1, len(A[i])):
        x[i] -= A[i][j] * x[j]

# Assign the results to the variables
a, c, e, g, i = x

# Print the results
print(f"麻 (a): {a} 錢")
print(f"麥 (c): {c} 錢")
print(f"菽 (e): {e} 錢")
print(f"答 (g): {g} 錢")
print(f"黍 (i): {i} 錢")


"""


### Explanation:
1. **Matrix Representation**: The system of equations is represented as a matrix `A` for coefficients and a vector `B` for constants.
2. **Gaussian Elimination**: We use Gaussian elimination to reduce the matrix to row echelon form and solve for the unknowns.
3. **Back Substitution**: After elimination, we solve for the unknowns starting from the last row.
4. **Fractions**: The `Fraction` class ensures that all calculations are exact and no precision is lost.

### Output:
The code will compute and print the prices per unit (斗) for 麻, 麥, 菽, 答, and 黍 in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: 4
Missing variable in output: 'd'
Variable 'e' has wrong value. Expected: 1, Actual: 3
Missing variable in output: 'f'
Variable 'g' has wrong value. Expected: 1, Actual: 5
Missing variable in output: 'h'
Variable 'i' has wrong value. Expected: 1, Actual: 6
Variable 'j' has wrong value. Expected: 6, Actual: 4"""
