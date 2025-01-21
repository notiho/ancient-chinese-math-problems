"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese mathematical methods, specifically the "正負術" (positive and negative method), which is equivalent to Gaussian elimination in modern terms. Here's the solution encoded in Python:


"""


from fractions import Fraction

# Problem setup
# Let the depth of the well be `井深 = a` (in 丈), and the rope lengths for each family be:
# 甲綆長 = b, 乙綆長 = c, 丙綆長 = d, 丁綆長 = e, 戊綆長 = f (all in 丈).

# The relationships are:
# 1. b - 2 = c - 1
# 2. c - 3 = d - 1
# 3. d - 4 = e - 1
# 4. e - 5 = f - 1
# 5. f - 6 = b - 1
# 6. Each family gets exactly one rope length (綆) to reach the bottom of the well.

# Convert these relationships into equations:
# b - c = -1
# c - d = -2
# d - e = -3
# e - f = -4
# f - b = -5

# Additionally, the depth of the well is the length of any rope plus the "不足" (shortfall):
# a = b + 2
# a = c + 3
# a = d + 4
# a = e + 5
# a = f + 6

# Matrix representation of the equations:
# Coefficients of b, c, d, e, f and constants
matrix = [
    [1, -1,  0,  0,  0, -1],  # b - c = -1
    [0,  1, -1,  0,  0, -2],  # c - d = -2
    [0,  0,  1, -1,  0, -3],  # d - e = -3
    [0,  0,  0,  1, -1, -4],  # e - f = -4
    [-1, 0,  0,  0,  1, -5],  # f - b = -5
]

# Solve the system of equations using Gaussian elimination
def gaussian_elimination(matrix):
    n = len(matrix)
    for i in range(n):
        # Make the diagonal element 1
        diag = matrix[i][i]
        for j in range(len(matrix[i])):
            matrix[i][j] = Fraction(matrix[i][j], diag)
        
        # Eliminate the current column for all other rows
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(len(matrix[k])):
                    matrix[k][j] -= factor * matrix[i][j]
    
    # Extract the solutions
    return [row[-1] for row in matrix]

# Perform Gaussian elimination
solutions = gaussian_elimination(matrix)

# Extract the rope lengths
b, c, d, e, f = solutions

# Calculate the depth of the well
a = b + 2

# Output the results
井深 = a
甲綆長 = b
乙綆長 = c
丙綆長 = d
丁綆長 = e
戊綆長 = f

井深, 甲綆長, 乙綆長, 丙綆長, 丁綆長, 戊綆長


"""


### Explanation:
1. The relationships between the rope lengths are converted into a system of linear equations.
2. Gaussian elimination is used to solve the system of equations.
3. The depth of the well (`井深`) is calculated based on any rope length plus its respective shortfall.
4. The results are presented as the depth of the well and the lengths of the ropes for each family.

### Answer:
The depth of the well is `a` 丈, and the rope lengths for 甲, 乙, 丙, 丁, and 戊 are `b`, `c`, `d`, `e`, and `f` 丈 respectively.
"""


"""
Code error: Fraction(0, 0)"""
