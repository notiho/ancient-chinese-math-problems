"""
今有麻九斗、麥七斗、菽三斗、答二斗、黍五斗，直錢一百四十；麻七斗、麥六斗、菽四斗、答五斗、黍三斗，直錢一百二十八；麻三斗、麥五斗、菽七斗、答六斗、黍四斗，直錢一百一十六；麻二斗、麥五斗、菽三斗、答九斗、黍四斗，直錢一百一十二；麻一斗、麥三斗、菽二斗、答八斗、黍五斗，直錢九十五。問︰一斗直幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：麻一斗 a錢 ，麥一斗 b錢 ，菽一斗 c錢 ，答一斗 d錢 ，黍一斗 e錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into a system of linear equations and solve it using Python. The problem involves finding the price per斗 (a unit of volume) for five grains: 麻 (a), 麥 (b), 菽 (c), 答 (d), and 黍 (e). The equations are derived from the given data.

Here is the Python code to compute the values of the unknowns:


"""


from fractions import Fraction

# Define the system of equations based on the problem:
# 9a + 7b + 3c + 2d + 5e = 140
# 7a + 6b + 4c + 5d + 3e = 128
# 3a + 5b + 7c + 6d + 4e = 116
# 2a + 5b + 3c + 9d + 4e = 112
# 1a + 3b + 2c + 8d + 5e = 95

# Coefficients matrix
A = [
    [9, 7, 3, 2, 5],
    [7, 6, 4, 5, 3],
    [3, 5, 7, 6, 4],
    [2, 5, 3, 9, 4],
    [1, 3, 2, 8, 5]
]

# Constants vector
B = [140, 128, 116, 112, 95]

# Solve the system of linear equations using Gaussian elimination
# Convert A and B into fractions for exact arithmetic
A = [[Fraction(x) for x in row] for row in A]
B = [Fraction(x) for x in B]

# Perform Gaussian elimination
n = len(A)
for i in range(n):
    # Make the diagonal element 1
    diag = A[i][i]
    for j in range(i, n):
        A[i][j] /= diag
    B[i] /= diag

    # Eliminate the current column in rows below
    for k in range(i + 1, n):
        factor = A[k][i]
        for j in range(i, n):
            A[k][j] -= factor * A[i][j]
        B[k] -= factor * B[i]

# Back substitution
x = [Fraction(0)] * n
for i in range(n - 1, -1, -1):
    x[i] = B[i]
    for j in range(i + 1, n):
        x[i] -= A[i][j] * x[j]

# Assign the solutions to the respective variables
a, b, c, d, e = x

# Print the results
print(f"麻 (a) = {a} 錢")
print(f"麥 (b) = {b} 錢")
print(f"菽 (c) = {c} 錢")
print(f"答 (d) = {d} 錢")
print(f"黍 (e) = {e} 錢")


"""


### Explanation:
1. **System of Equations**: The problem gives us five equations with five unknowns (a, b, c, d, e). These equations are represented in matrix form as \(Ax = B\), where \(A\) is the coefficients matrix, \(x\) is the vector of unknowns, and \(B\) is the constants vector.
2. **Gaussian Elimination**: We use Gaussian elimination to solve the system of linear equations. This involves forward elimination to make the matrix upper triangular and back substitution to find the solutions.
3. **Fractions**: The `Fraction` class is used to ensure exact arithmetic, as the solutions might not be integers.

### Output:
The code will compute and print the values of \(a\), \(b\), \(c\), \(d\), and \(e\) in terms of 錢 (money).
"""


"""
"""
