"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem involves a system of linear equations, which is solved using the ancient Chinese method of elimination, similar to Gaussian elimination. Below is the solution translated into Python code.


"""


from fractions import Fraction

# Problem setup:
# Let the depth of the well be `井深 = a` (in zhang), and the rope lengths for each family be:
# 甲綆長 = b, 乙綆長 = c, 丙綆長 = d, 丁綆長 = e, 戊綆長 = f (all in zhang).

# The relationships are:
# 1. b - 2 = c - 1
# 2. c - 3 = d - 1
# 3. d - 4 = e - 1
# 4. e - 5 = f - 1
# 5. f - 6 = b - 1
# 6. a = b + 1 (井深 equals the length of the rope for 甲 plus 1 zhang).

# Step 1: Represent the equations in terms of variables.
# Let the unknowns be [a, b, c, d, e, f].
# The equations can be written as:
# b - c = -1
# c - d = -2
# d - e = -3
# e - f = -4
# f - b = -5
# a - b = 1

# Step 2: Write the augmented matrix for the system of equations.
# Coefficients of [a, b, c, d, e, f] and the constant terms:
matrix = [
    [0, 1, -1,  0,  0,  0, -1],  # b - c = -1
    [0, 0,  1, -1,  0,  0, -2],  # c - d = -2
    [0, 0,  0,  1, -1,  0, -3],  # d - e = -3
    [0, 0,  0,  0,  1, -1, -4],  # e - f = -4
    [0, -1, 0,  0,  0,  1, -5],  # f - b = -5
    [1, -1, 0,  0,  0,  0,  1],  # a - b = 1
]

# Step 3: Perform Gaussian elimination to solve the system.

def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Forward elimination
    for i in range(rows):
        # Make the diagonal element 1
        diag = matrix[i][i]
        for j in range(cols):
            matrix[i][j] = Fraction(matrix[i][j], diag)

        # Eliminate the current column in rows below
        for k in range(i + 1, rows):
            factor = matrix[k][i]
            for j in range(cols):
                matrix[k][j] -= factor * matrix[i][j]

    # Back substitution
    for i in range(rows - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            factor = matrix[k][i]
            for j in range(cols):
                matrix[k][j] -= factor * matrix[i][j]

    # Extract the solutions
    return [matrix[i][-1] for i in range(rows)]

# Solve the system
solution = gaussian_elimination(matrix)

# Extract the results
a = solution[0]  # 井深
b = solution[1]  # 甲綆長
c = solution[2]  # 乙綆長
d = solution[3]  # 丙綆長
e = solution[4]  # 丁綆長
f = solution[5]  # 戊綆長

# Convert the results to zhang and chi (1 zhang = 10 chi)
井深 = a
甲綆長 = b
乙綆長 = c
丙綆長 = d
丁綆長 = e
戊綆長 = f * 10  # Convert to chi

# Output the results
井深, 甲綆長, 乙綆長, 丙綆長, 丁綆長, 戊綆長


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as an augmented matrix, where each row corresponds to one equation.
2. **Gaussian Elimination**: The matrix is solved using forward elimination to make it upper triangular, followed by back substitution to find the solutions.
3. **Fraction Handling**: The `Fraction` class is used to ensure exact arithmetic throughout the calculations.
4. **Unit Conversion**: The results are converted to the appropriate units (zhang and chi) for the final answer.

### Final Answer:
The depth of the well (`井深`) and the rope lengths for each family (`甲綆長`, `乙綆長`, `丙綆長`, `丁綆長`, `戊綆長`) are calculated and output in the correct units.
"""


"""
Code error: Fraction(0, 0)"""
