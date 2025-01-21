"""
今有白禾二步青禾三步黃禾四步黑禾五步實各不滿斗白取青黃青取黃黑黃取黑白黑取白青各一步而實滿斗問白青黃黑禾實一步各幾何
術曰如方程各置所取以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰白禾 a步 實 b斗 青禾 c步 實 d斗 黃禾 e步 實 f斗 黑禾 g步 實 h斗 
"""

"""
This problem involves solving a system of linear equations using an ancient Chinese method described in the "Nine Chapters on the Mathematical Art." The problem essentially asks for the contributions of each type of grain (white, green, yellow, black) to a full dou of grain, given specific proportions of exchange between them.

Let's break this down step by step and implement it in Python:


"""


from fractions import Fraction

# Problem setup
# White (白禾), Green (青禾), Yellow (黃禾), Black (黑禾)
# Each type of grain contributes a certain number of steps to fill one dou of grain.
# We are solving for the contribution of each type of grain.

# Coefficients of the system of equations
# Each row represents the exchange relationships for one type of grain.
# For example, white takes green and yellow, green takes yellow and black, etc.
coefficients = [
    [1, -1, -1, 0],  # White takes green and yellow
    [0, 1, -1, -1],  # Green takes yellow and black
    [0, 0, 1, -1],   # Yellow takes black and white
    [-1, 0, 0, 1]    # Black takes white and green
]

# Right-hand side of the equations (the total dou of grain)
rhs = [1, 1, 1, 1]  # Each type of grain contributes to one dou

# Solve the system of equations using the ancient method
# Step 1: Normalize the first row
for i in range(4):
    coefficients[0][i] = Fraction(coefficients[0][i], coefficients[0][0])
rhs[0] = Fraction(rhs[0], coefficients[0][0])

# Step 2: Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = coefficients[i][0]
    for j in range(4):
        coefficients[i][j] -= factor * coefficients[0][j]
    rhs[i] -= factor * rhs[0]

# Step 3: Normalize the second row
for i in range(1, 4):
    coefficients[1][i] = Fraction(coefficients[1][i], coefficients[1][1])
rhs[1] = Fraction(rhs[1], coefficients[1][1])

# Step 4: Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = coefficients[i][1]
    for j in range(1, 4):
        coefficients[i][j] -= factor * coefficients[1][j]
    rhs[i] -= factor * rhs[1]

# Step 5: Normalize the third row
for i in range(2, 4):
    coefficients[2][i] = Fraction(coefficients[2][i], coefficients[2][2])
rhs[2] = Fraction(rhs[2], coefficients[2][2])

# Step 6: Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = coefficients[i][2]
    for j in range(2, 4):
        coefficients[i][j] -= factor * coefficients[2][j]
    rhs[i] -= factor * rhs[2]

# Step 7: Normalize the fourth row
coefficients[3][3] = Fraction(coefficients[3][3], coefficients[3][3])
rhs[3] = Fraction(rhs[3], coefficients[3][3])

# Step 8: Back-substitute to find the solution
a = rhs[0]
b = rhs[1]
c = rhs[2]
d = rhs[3]

# Output the results
print(f"白禾 {a}步 實 {a}斗")
print(f"青禾 {b}步 實 {b}斗")
print(f"黃禾 {c}步 實 {c}斗")
print(f"黑禾 {d}步 實 {d}斗")


"""


This code implements the ancient Chinese method for solving systems of linear equations, as described in the problem. The solution gives the contribution of each type of grain (in steps and dou) to a full dou of grain.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 4
Variable 'b' has wrong value. Expected: 11/37, Actual: 2
Variable 'd' has wrong value. Expected: 28/111, Actual: 5
Missing variable in output: 'e'
Missing variable in output: 'f'
Missing variable in output: 'g'
Missing variable in output: 'h'"""
