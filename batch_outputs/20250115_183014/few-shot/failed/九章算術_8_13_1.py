"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This problem is essentially a system of linear equations, where the relationships between the different types of grains (white, green, yellow, and black) are given. The solution involves using the ancient Chinese method of solving simultaneous equations, which is similar to Gaussian elimination. Let's translate the procedure into Python code.


"""


from fractions import Fraction

# Define the coefficients of the equations based on the problem
# Each row corresponds to an equation, and each column corresponds to a variable (white, green, yellow, black)
# The last column represents the total (right-hand side of the equation)
matrix = [
    [1, -1, -1, 0, 0],  # White takes Green and Yellow
    [0, 1, -1, -1, 0],  # Green takes Yellow and Black
    [0, 0, 1, -1, -1],  # Yellow takes Black and White
    [-1, 0, 0, 1, 0],   # Black takes White and Green
    [1, 1, 1, 1, 1]     # Total sum of all steps equals 1 dou
]

# Convert the matrix into fractions for precise calculations
matrix = [[Fraction(x) for x in row] for row in matrix]

# Perform Gaussian elimination to solve the system of equations
# Step 1: Forward elimination
for i in range(4):  # There are 4 variables (white, green, yellow, black)
    # Make the diagonal element 1 by dividing the entire row
    diag = matrix[i][i]
    for j in range(5):  # There are 5 columns (4 variables + 1 total)
        matrix[i][j] /= diag

    # Eliminate the current variable from the rows below
    for k in range(i + 1, 4):
        factor = matrix[k][i]
        for j in range(5):
            matrix[k][j] -= factor * matrix[i][j]

# Step 2: Back substitution
for i in range(3, -1, -1):  # Start from the last variable and move upwards
    for k in range(i - 1, -1, -1):
        factor = matrix[k][i]
        for j in range(5):
            matrix[k][j] -= factor * matrix[i][j]

# Extract the solutions
white = matrix[0][4]
green = matrix[1][4]
yellow = matrix[2][4]
black = matrix[3][4]

# Output the results
a, b = 2, white
c, d = 3, green
e, f = 4, yellow
g, h = 5, black

print(f"白禾 {a}步 實 {b}斗")
print(f"青禾 {c}步 實 {d}斗")
print(f"黃禾 {e}步 實 {f}斗")
print(f"黑禾 {g}步 實 {h}斗")


"""


### Explanation of the Code:
1. **Matrix Representation**: The problem is represented as a system of linear equations. Each equation corresponds to the relationships described in the problem.
2. **Gaussian Elimination**: The ancient Chinese method of solving simultaneous equations is similar to Gaussian elimination, where we eliminate variables row by row to simplify the system.
3. **Back Substitution**: After forward elimination, we solve for each variable starting from the last row and moving upwards.
4. **Fractions**: The `Fraction` class is used to ensure precise calculations without floating-point errors.

### Final Answer:
The solution will provide the amounts of each type of grain (white, green, yellow, black) in dou (斗).
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 2
Variable 'b' has wrong value. Expected: 11/37, Actual: 1
Variable 'c' has wrong value. Expected: 1, Actual: 3
Variable 'd' has wrong value. Expected: 28/111, Actual: 1
Variable 'e' has wrong value. Expected: 1, Actual: 4
Variable 'f' has wrong value. Expected: 17/111, Actual: 0
Variable 'g' has wrong value. Expected: 1, Actual: 5
Variable 'h' has wrong value. Expected: 10/111, Actual: 1"""
