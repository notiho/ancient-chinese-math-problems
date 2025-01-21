"""
今有五家共井甲二綆不足如乙一綆乙三綆不足如丙一綆丙四綆不足如丁一綆丁五綆不足如戊一綆戊六綆不足如甲一綆如各得所不足一綆皆逮問井深綆長各幾何
術曰如方程以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰井深 a丈 甲綆長 b丈 乙綆長 c丈 丙綆長 d丈 丁綆長 e丈 戊綆長 f尺 
"""

"""
This problem involves solving a system of linear equations using ancient Chinese "fangcheng" (方程) methods, which is an early form of matrix manipulation. The problem is complex, but I will translate it into Python code step by step, adhering to the procedure described.

### Problem Explanation:
There are five households sharing a well. Each household's rope is insufficient by a certain amount to reach the water, and the insufficiency is described in terms of the next household's rope. The goal is to determine the depth of the well and the length of each household's rope.

### Procedure:
The "fangcheng" method involves setting up a system of equations and solving it using elimination techniques. The procedure is described in the problem statement, and I will encode it step by step.

### Python Code:


"""


from fractions import Fraction

# Step 1: Define the system of equations based on the problem.
# Let the variables be:
# a = depth of the well (in zhang)
# b = length of rope for household A (in zhang)
# c = length of rope for household B (in zhang)
# d = length of rope for household C (in zhang)
# e = length of rope for household D (in zhang)
# f = length of rope for household E (in zhang)

# The equations are:
# 1. b + 2 = c
# 2. c + 3 = d
# 3. d + 4 = e
# 4. e + 5 = f
# 5. f + 6 = b + a

# Step 2: Represent the equations in matrix form.
# Coefficients of the variables [a, b, c, d, e, f] and the constants on the right-hand side.
matrix = [
    [0, 1, -1, 0, 0, 0],  # b - c = -2
    [0, 0, 1, -1, 0, 0],  # c - d = -3
    [0, 0, 0, 1, -1, 0],  # d - e = -4
    [0, 0, 0, 0, 1, -1],  # e - f = -5
    [1, -1, 0, 0, 0, 1],  # a + f - b = 6
]

constants = [-2, -3, -4, -5, 6]

# Step 3: Solve the system of equations using Gaussian elimination.
def gaussian_elimination(matrix, constants):
    n = len(matrix)
    # Forward elimination
    for i in range(n):
        # Make the diagonal element 1
        diag = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] = Fraction(matrix[i][j], diag)
        constants[i] = Fraction(constants[i], diag)
        # Eliminate the current variable from the rows below
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n):
                matrix[k][j] -= factor * matrix[i][j]
            constants[k] -= factor * constants[i]
    # Back substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = constants[i]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
    return solution

# Solve the system
solution = gaussian_elimination(matrix, constants)

# Step 4: Extract the results.
a = solution[0]  # Depth of the well (in zhang)
b = solution[1]  # Length of rope for household A (in zhang)
c = solution[2]  # Length of rope for household B (in zhang)
d = solution[3]  # Length of rope for household C (in zhang)
e = solution[4]  # Length of rope for household D (in zhang)
f = solution[5]  # Length of rope for household E (in zhang)

# Convert f to chi (1 zhang = 10 chi)
f_in_chi = f * 10

# Print the results
print(f"井深 {a}丈")
print(f"甲綆長 {b}丈")
print(f"乙綆長 {c}丈")
print(f"丙綆長 {d}丈")
print(f"丁綆長 {e}丈")
print(f"戊綆長 {f_in_chi}尺")


"""


### Explanation of the Code:
1. **Matrix Representation**: The system of equations is represented as a matrix with coefficients of the variables and a separate list for the constants.
2. **Gaussian Elimination**: The system is solved using Gaussian elimination, which involves forward elimination to make the matrix upper triangular and back substitution to find the solution.
3. **Conversion**: The length of the rope for household E (`f`) is converted from zhang to chi (1 zhang = 10 chi).
4. **Output**: The results are printed in the required format.

### Answer:
The code will compute the depth of the well (`a`) and the lengths of the ropes (`b`, `c`, `d`, `e`, `f`) based on the given relationships.
"""


"""
Code error: Fraction(0, 0)"""
