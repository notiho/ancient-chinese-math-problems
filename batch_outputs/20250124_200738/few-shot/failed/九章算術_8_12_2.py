"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
術曰：如方程，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This problem involves solving a system of equations using ancient Chinese methods, specifically the "正負術" (positive-negative method), which is an early form of Gaussian elimination. Here's how we can translate the problem into Python code:

### Problem Breakdown:
1. There are five families (甲, 乙, 丙, 丁, 戊) sharing a well.
2. Each family's rope length is insufficient by a certain amount to reach the well's depth, but when combined with another family's rope length, it suffices.
3. The relationships are as follows:
   - 甲's rope is 2 units short of 乙's rope.
   - 乙's rope is 3 units short of 丙's rope.
   - 丙's rope is 4 units short of 丁's rope.
   - 丁's rope is 5 units short of 戊's rope.
   - 戊's rope is 6 units short of 甲's rope.
4. The goal is to find the well's depth and the length of each family's rope.

### Procedure:
We will set up a system of equations based on the relationships and solve it using the described method.


"""

#----- content starts here -----

from fractions import Fraction

# Define the relationships as equations
# Let the well's depth be `井深 = a` and the rope lengths be:
# 甲綆 = b, 乙綆 = c, 丙綆 = d, 丁綆 = e, 戊綆 = f

# Equations based on the problem:
# 1. b + 2 = c
# 2. c + 3 = d
# 3. d + 4 = e
# 4. e + 5 = f
# 5. f + 6 = b + a

# Rewrite the equations in terms of `a` (井深) and the rope lengths:
# b - c = -2
# c - d = -3
# d - e = -4
# e - f = -5
# f - b = -6 + a

# Represent the system of equations as a matrix:
# Coefficients of [b, c, d, e, f, a]
matrix = [
    [1, -1,  0,  0,  0,  0, -2],  # b - c = -2
    [0,  1, -1,  0,  0,  0, -3],  # c - d = -3
    [0,  0,  1, -1,  0,  0, -4],  # d - e = -4
    [0,  0,  0,  1, -1,  0, -5],  # e - f = -5
    [-1, 0,  0,  0,  1,  1, -6],  # f - b = -6 + a
]

# Perform Gaussian elimination to solve the system
def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Forward elimination
    for i in range(rows):
        # Normalize the pivot row
        pivot = matrix[i][i]
        for j in range(cols):
            matrix[i][j] = Fraction(matrix[i][j], pivot)

        # Eliminate the current column in rows below
        for k in range(i + 1, rows):
            factor = matrix[k][i]
            for j in range(cols):
                matrix[k][j] -= factor * matrix[i][j]

    # Back substitution
    solution = [0] * (cols - 1)
    for i in range(rows - 1, -1, -1):
        solution[i] = matrix[i][-1]
        for j in range(i + 1, cols - 1):
            solution[i] -= matrix[i][j] * solution[j]

    return solution

# Solve the system
solution = gaussian_elimination(matrix)

# Extract the results
b, c, d, e, f, a = solution

# Convert the well depth (a) to 丈 and rope lengths to 丈 and 尺
井深 = a
甲綆 = b
乙綆 = c
丙綆 = d
丁綆 = e
戊綆 = f

# Output the results
print(f"井深 {井深} 丈")
print(f"甲綆長 {甲綆} 丈")
print(f"乙綆長 {乙綆} 丈")
print(f"丙綆長 {丙綆} 丈")
print(f"丁綆長 {丁綆} 丈")
print(f"戊綆長 {戊綆} 丈")
#----- content ends here -----


"""


### Explanation:
1. The system of equations is represented as a matrix, where each row corresponds to an equation.
2. Gaussian elimination is used to solve the system step by step:
   - Normalize the pivot row.
   - Eliminate the current column in rows below.
   - Perform back substitution to find the solution.
3. The solution gives the well's depth (`井深`) and the rope lengths (`甲綆`, `乙綆`, `丙綆`, `丁綆`, `戊綆`).
4. The results are converted to the appropriate units (丈 and 尺) for the final answer.
"""


"""
Code error: Fraction(0, 0)"""
