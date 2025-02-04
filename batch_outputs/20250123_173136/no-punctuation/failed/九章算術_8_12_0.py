"""
今有五家共井甲二綆不足如乙一綆乙三綆不足如丙一綆丙四綆不足如丁一綆丁五綆不足如戊一綆戊六綆不足如甲一綆如各得所不足一綆皆逮問井深綆長各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰井深 a丈 甲綆長 b丈 乙綆長 c丈 丙綆長 d丈 丁綆長 e丈 戊綆長 f尺 
"""

"""
This problem involves solving a system of equations using ancient Chinese "fangcheng" (方程) or matrix methods. The problem is complex and involves iterative calculations. Below is the Python implementation of the procedure described in the problem, following the ancient method step by step.


"""


from fractions import Fraction

# Problem setup
# Let the unknowns be:
# a = depth of the well (井深)
# b = length of rope for A (甲綆長)
# c = length of rope for B (乙綆長)
# d = length of rope for C (丙綆長)
# e = length of rope for D (丁綆長)
# f = length of rope for E (戊綆長)

# The equations based on the problem:
# 1. a - b = 2
# 2. a - c = 3
# 3. a - d = 4
# 4. a - e = 5
# 5. a - f = 6
# 6. f - b = 1

# Using the ancient "fangcheng" method to solve this system of equations.

# Step 1: Represent the equations in matrix form
# Coefficients of the variables [a, b, c, d, e, f]
matrix = [
    [1, -1,  0,  0,  0,  0],  # a - b = 2
    [1,  0, -1,  0,  0,  0],  # a - c = 3
    [1,  0,  0, -1,  0,  0],  # a - d = 4
    [1,  0,  0,  0, -1,  0],  # a - e = 5
    [1,  0,  0,  0,  0, -1],  # a - f = 6
    [0, -1,  0,  0,  0,  1],  # f - b = 1
]

# Constants on the right-hand side
constants = [2, 3, 4, 5, 6, 1]

# Step 2: Solve using Gaussian elimination (ancient method)
# Convert the matrix to row echelon form
for i in range(len(matrix)):
    # Make the diagonal element 1 by dividing the entire row
    diag_element = matrix[i][i]
    for j in range(len(matrix[i])):
        matrix[i][j] = Fraction(matrix[i][j], diag_element)
    constants[i] = Fraction(constants[i], diag_element)
    
    # Eliminate the current variable from all rows below
    for k in range(i + 1, len(matrix)):
        factor = matrix[k][i]
        for j in range(len(matrix[k])):
            matrix[k][j] -= factor * matrix[i][j]
        constants[k] -= factor * constants[i]

# Step 3: Back substitution to find the solution
solution = [0] * len(matrix)
for i in range(len(matrix) - 1, -1, -1):
    solution[i] = constants[i]
    for j in range(i + 1, len(matrix)):
        solution[i] -= matrix[i][j] * solution[j]

# Extract the solutions
a = solution[0]  # Depth of the well
b = solution[1]  # Length of rope for A
c = solution[2]  # Length of rope for B
d = solution[3]  # Length of rope for C
e = solution[4]  # Length of rope for D
f = solution[5]  # Length of rope for E

# Convert the depth (a) to zhang (1 zhang = 10 chi)
a = Fraction(a, 10)

# Output the results
print(f"井深 {a}丈")
print(f"甲綆長 {b}丈")
print(f"乙綆長 {c}丈")
print(f"丙綆長 {d}丈")
print(f"丁綆長 {e}丈")
print(f"戊綆長 {f}尺")


"""


### Explanation of the Code:
1. **Matrix Representation**: The equations are represented in matrix form, with coefficients of the variables and constants on the right-hand side.
2. **Gaussian Elimination**: The ancient "fangcheng" method is equivalent to Gaussian elimination, where the matrix is reduced to row echelon form.
3. **Back Substitution**: Once the matrix is in row echelon form, the solutions are found using back substitution.
4. **Unit Conversion**: The depth of the well (`a`) is converted from chi to zhang, as 1 zhang = 10 chi.

### Final Answer:
The program will output the depth of the well (`a`) in zhang and the lengths of the ropes (`b`, `c`, `d`, `e`, `f`) in chi or zhang as appropriate.
"""


"""
Code error: Fraction(0, 0)"""
