"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese procedure into Python code step by step. The problem involves solving a system of linear equations using the described method. Here's the implementation:


"""


from fractions import Fraction

# Step 1: Define the system of equations based on the problem
# Let the unknowns be:
# x = white禾實 (白禾實一步)
# y = green禾實 (青禾實一步)
# z = yellow禾實 (黃禾實一步)
# w = black禾實 (黑禾實一步)

# The equations are derived from the problem:
# White禾: x + y + z = 1
# Green禾: y + z + w = 1
# Yellow禾: z + w + x = 1
# Black禾: w + x + y = 1

# Step 2: Represent the equations in matrix form
# Coefficients matrix:
A = [
    [1, 1, 1, 0],  # x + y + z = 1
    [0, 1, 1, 1],  # y + z + w = 1
    [1, 0, 1, 1],  # z + w + x = 1
    [1, 1, 0, 1],  # w + x + y = 1
]

# Constants on the right-hand side:
B = [1, 1, 1, 1]

# Step 3: Solve the system of equations using the described method
# Initialize variables
x, y, z, w = 0, 0, 0, 0

# Use the elimination method described in the procedure
# First, eliminate variables step by step

# Eliminate x from the second, third, and fourth equations
for i in range(1, 4):
    factor = Fraction(A[i][0], A[0][0])
    for j in range(4):
        A[i][j] -= factor * A[0][j]
    B[i] -= factor * B[0]

# Eliminate y from the third and fourth equations
for i in range(2, 4):
    factor = Fraction(A[i][1], A[1][1])
    for j in range(4):
        A[i][j] -= factor * A[1][j]
    B[i] -= factor * B[1]

# Eliminate z from the fourth equation
factor = Fraction(A[3][2], A[2][2])
for j in range(4):
    A[3][j] -= factor * A[2][j]
B[3] -= factor * B[2]

# Step 4: Back-substitute to find the values of the variables
w = Fraction(B[3], A[3][3])
z = Fraction(B[2] - A[2][3] * w, A[2][2])
y = Fraction(B[1] - A[1][2] * z - A[1][3] * w, A[1][1])
x = Fraction(B[0] - A[0][1] * y - A[0][2] * z - A[0][3] * w, A[0][0])

# Step 5: Output the results
a, b = 1, x  # White禾: 1步, 实x斗
c, d = 1, y  # Green禾: 1步, 实y斗
e, f = 1, z  # Yellow禾: 1步, 实z斗
g, h = 1, w  # Black禾: 1步, 实w斗

print(f"白禾 {a}步 實 {b}斗")
print(f"青禾 {c}步 實 {d}斗")
print(f"黃禾 {e}步 實 {f}斗")
print(f"黑禾 {g}步 實 {h}斗")


"""


### Explanation:
1. **Matrix Representation**: The equations are represented in matrix form for clarity and to facilitate elimination.
2. **Elimination Method**: The procedure described in the problem is essentially Gaussian elimination, where variables are eliminated step by step.
3. **Back-Substitution**: After elimination, the variables are solved starting from the last equation and substituting back into the previous ones.
4. **Fraction Representation**: The `Fraction` class is used to ensure exact arithmetic, as required by the problem.

### Output:
The solution will provide the values of `x`, `y`, `z`, and `w`, which represent the 实 (actual斗) for each type of 禾.
"""


"""
Variable 'b' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'd' has wrong value. Expected: 28/111, Actual: 1/3
Variable 'f' has wrong value. Expected: 17/111, Actual: 1/3
Variable 'h' has wrong value. Expected: 10/111, Actual: 1/3"""
