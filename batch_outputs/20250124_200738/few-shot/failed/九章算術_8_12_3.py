"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem involves a system of linear equations, which is solved using the ancient Chinese method of elimination, similar to Gaussian elimination. Below is the solution translated into Python code.

### Problem Description
- Five families share a well.
- The rope lengths are related as follows:
  - Family A's rope is 2 units too short, but if extended by Family B's rope length, it is sufficient.
  - Family B's rope is 3 units too short, but if extended by Family C's rope length, it is sufficient.
  - Family C's rope is 4 units too short, but if extended by Family D's rope length, it is sufficient.
  - Family D's rope is 5 units too short, but if extended by Family E's rope length, it is sufficient.
  - Family E's rope is 6 units too short, but if extended by Family A's rope length, it is sufficient.
- Each family should have exactly the length they are short by.

The goal is to find the depth of the well and the length of each family's rope.

---

### Solution Procedure
The problem is modeled as a system of linear equations:
1. \( A + 2 = B \)
2. \( B + 3 = C \)
3. \( C + 4 = D \)
4. \( D + 5 = E \)
5. \( E + 6 = A \)

We solve this system using the elimination method described in the "方程術" (method of equations).

---

### Python Code


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Represent the system of equations in matrix form
# Coefficients of the variables (A, B, C, D, E)
matrix = [
    [1, -1, 0, 0, 0],  # A - B = -2
    [0, 1, -1, 0, 0],  # B - C = -3
    [0, 0, 1, -1, 0],  # C - D = -4
    [0, 0, 0, 1, -1],  # D - E = -5
    [-1, 0, 0, 0, 1]   # E - A = -6
]

# Constants on the right-hand side of the equations
constants = [-2, -3, -4, -5, -6]

# Step 2: Perform Gaussian elimination
# Convert the matrix to row echelon form
for i in range(len(matrix)):
    # Normalize the pivot row
    pivot = matrix[i][i]
    for j in range(len(matrix[i])):
        matrix[i][j] = Fraction(matrix[i][j], pivot)
    constants[i] = Fraction(constants[i], pivot)
    
    # Eliminate the current variable from the rows below
    for k in range(i + 1, len(matrix)):
        factor = matrix[k][i]
        for j in range(len(matrix[k])):
            matrix[k][j] -= factor * matrix[i][j]
        constants[k] -= factor * constants[i]

# Step 3: Back substitution to solve for the variables
variables = [0] * len(constants)
for i in range(len(matrix) - 1, -1, -1):
    variables[i] = constants[i]
    for j in range(i + 1, len(matrix)):
        variables[i] -= matrix[i][j] * variables[j]

# Step 4: Interpret the results
# The variables represent the lengths of the ropes for A, B, C, D, and E
A = variables[0]
B = variables[1]
C = variables[2]
D = variables[3]
E = variables[4]

# The depth of the well is the length of any rope plus its respective shortfall
well_depth = A + 2  # or equivalently B + 3, C + 4, etc.

# Convert results to the required units (丈 for ropes, 尺 for the remainder)
a = well_depth  # Depth of the well in 丈
b = A  # Rope length for A in 丈
c = B  # Rope length for B in 丈
d = C  # Rope length for C in 丈
e = D  # Rope length for D in 丈
f = E  # Rope length for E in 丈

# Output the results
print(f"井深 {a}丈 。甲綆長 {b}丈 ，乙綆長 {c}丈 ，丙綆長 {d}丈 ，丁綆長 {e}丈 ，戊綆長 {f}丈 。")
#----- content ends here -----


"""


---

### Explanation of the Code
1. **Matrix Representation**: The system of equations is represented as a matrix where each row corresponds to an equation.
2. **Gaussian Elimination**: The matrix is reduced to row echelon form, and back substitution is used to solve for the variables.
3. **Interpretation**: The variables represent the rope lengths, and the depth of the well is calculated based on the shortfall of any rope.

---

### Final Answer
The output will provide the depth of the well and the lengths of the ropes for each family in 丈 (zhang).
"""


"""
Code error: Fraction(0, 0)"""
