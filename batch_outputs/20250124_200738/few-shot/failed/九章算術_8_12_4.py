"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical techniques, specifically the "正負術" (positive and negative method), which is equivalent to Gaussian elimination. Here's how we can translate the problem into Python code:

### Problem Breakdown:
- Five families share a well.
- Each family has a rope of a certain length, but their ropes are insufficient to reach the bottom of the well.
- The insufficiency of each family's rope is described in terms of the next family's rope.
- We need to find the depth of the well (井深) and the length of each family's rope.

### Procedure:
1. Represent the relationships as a system of linear equations.
2. Use the ancient "正負術" (Gaussian elimination) to solve the equations.

### Translation into Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the system of equations based on the problem:
# Let the depth of the well be `井深 = a` (in 丈).
# Let the rope lengths of 甲, 乙, 丙, 丁, 戊 be `b, c, d, e, f` (in 丈).
# The equations are:
# 1. a = b + 2
# 2. a = c + 3
# 3. a = d + 4
# 4. a = e + 5
# 5. a = f + 6
# 6. f = b + 1

# Step 1: Represent the equations in matrix form (augmented matrix):
# Coefficients of [a, b, c, d, e, f] and the constants on the right-hand side.
matrix = [
    [1, -1,  0,  0,  0,  0,  2],  # a - b = 2
    [1,  0, -1,  0,  0,  0,  3],  # a - c = 3
    [1,  0,  0, -1,  0,  0,  4],  # a - d = 4
    [1,  0,  0,  0, -1,  0,  5],  # a - e = 5
    [1,  0,  0,  0,  0, -1,  6],  # a - f = 6
    [0,  1,  0,  0,  0, -1, -1],  # b - f = -1
]

# Step 2: Perform Gaussian elimination to solve the system of equations.

def gaussian_elimination(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Forward elimination
    for i in range(n):
        # Make the diagonal element 1
        diag = matrix[i][i]
        for j in range(m):
            matrix[i][j] = Fraction(matrix[i][j], diag)
        
        # Eliminate the current column in rows below
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(m):
                matrix[k][j] -= factor * matrix[i][j]

    # Back substitution
    for i in range(n - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            factor = matrix[k][i]
            for j in range(m):
                matrix[k][j] -= factor * matrix[i][j]

    # Extract the solutions
    return [matrix[i][-1] for i in range(n)]

# Solve the system
solutions = gaussian_elimination(matrix)

# Extract the results
井深 = solutions[0]  # a
甲綆長 = solutions[1]  # b
乙綆長 = solutions[2]  # c
丙綆長 = solutions[3]  # d
丁綆長 = solutions[4]  # e
戊綆長 = solutions[5]  # f

# Output the results
a = 井深
b = 甲綆長
c = 乙綆長
d = 丙綆長
e = 丁綆長
f = 戊綆長

# Print the results
print(f"井深 {a}丈 。甲綆長 {b}丈 ，乙綆長 {c}丈 ，丙綆長 {d}丈 ，丁綆長 {e}丈 ，戊綆長 {f}丈 。")
#----- content ends here -----


"""


### Explanation:
1. The system of equations is represented as an augmented matrix.
2. Gaussian elimination is performed to reduce the matrix to row-echelon form and then solve for the variables.
3. The results are extracted and printed in the required format.

### Answer:
The depth of the well (井深) and the lengths of the ropes (甲綆長, 乙綆長, 丙綆長, 丁綆長, 戊綆長) are calculated and displayed.
"""


"""
Code error: Fraction(0, 0)"""
