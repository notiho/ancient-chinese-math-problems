"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This problem is a classic system of linear equations, and the solution involves solving for the unknowns using elimination and substitution. Below is the Python implementation of the described procedure:


"""


from fractions import Fraction

# Step 1: Define the coefficients of the system of equations
# White (白禾), Green (青禾), Yellow (黃禾), Black (黑禾)
# Each equation represents the total contribution of each type of grain to the full斗.
# White takes from Green and Yellow, Green takes from Yellow and Black, etc.
# Coefficients are based on the problem description.

# Coefficients for the equations
# White: 1 White - 1 Green - 1 Yellow = 0
# Green: 1 Green - 1 Yellow - 1 Black = 0
# Yellow: 1 Yellow - 1 Black - 1 White = 0
# Black: 1 Black - 1 White - 1 Green = 1 (since the total斗 is full)

# Representing the system of equations as a matrix
# Each row corresponds to an equation, and the last column is the constant term.
matrix = [
    [1, -1, -1, 0, 0],  # White equation
    [0, 1, -1, -1, 0],  # Green equation
    [-1, 0, 1, -1, 0],  # Yellow equation
    [-1, -1, 0, 1, 1],  # Black equation
]

# Step 2: Perform Gaussian elimination to solve the system of equations
# Convert the matrix to row echelon form
for i in range(4):
    # Normalize the current row
    divisor = matrix[i][i]
    for j in range(5):
        matrix[i][j] = Fraction(matrix[i][j], divisor)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, 4):
        factor = matrix[k][i]
        for j in range(5):
            matrix[k][j] -= factor * matrix[i][j]

# Back substitution to find the solution
solution = [0, 0, 0, 0]
for i in range(3, -1, -1):
    solution[i] = matrix[i][4]
    for j in range(i + 1, 4):
        solution[i] -= matrix[i][j] * solution[j]

# Step 3: Extract the results
a, c, e, g = 1, 1, 1, 1  # Steps for each type of grain (all are 1 step as per the problem)
b, d, f, h = solution    # Corresponding斗 for each type of grain

# Output the results
print(f"白禾 {a}步 實 {b}斗")
print(f"青禾 {c}步 實 {d}斗")
print(f"黃禾 {e}步 實 {f}斗")
print(f"黑禾 {g}步 實 {h}斗")


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix, where each row corresponds to an equation, and the last column is the constant term.
2. **Gaussian Elimination**: The matrix is reduced to row echelon form to solve for the variables step by step.
3. **Back Substitution**: The solution is obtained by substituting the known values back into the equations.
4. **Output**: The results are printed, showing the steps and斗 for each type of grain.

### Results:
The solution will provide the斗 (实) for each type of grain (白禾, 青禾, 黄禾, 黑禾) based on the problem's constraints.
"""


"""
Variable 'b' has wrong value. Expected: 11/37, Actual: -3/5
Variable 'd' has wrong value. Expected: 28/111, Actual: -1/5
Variable 'f' has wrong value. Expected: 17/111, Actual: -2/5
Variable 'h' has wrong value. Expected: 10/111, Actual: 1/5"""
