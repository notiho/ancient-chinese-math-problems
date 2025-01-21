"""
今有白禾二步青禾三步黃禾四步黑禾五步實各不滿斗白取青黃青取黃黑黃取黑白黑取白青各一步而實滿斗問白青黃黑禾實一步各幾何
術曰如方程各置所取以正負術入之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰白禾 a步 實 b斗 青禾 c步 實 d斗 黃禾 e步 實 f斗 黑禾 g步 實 h斗 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese "fangcheng" (方程) method. The problem describes a situation where four types of grains (white, green, yellow, and black) are mixed in specific proportions, and the total volume of the mixture is one dou. The goal is to determine how much of each type of grain is present in one step.

Here is the solution encoded in Python:


"""


from fractions import Fraction

# Problem setup
# White grain (白禾), Green grain (青禾), Yellow grain (黃禾), Black grain (黑禾)
# Steps for each: 白禾取青黃, 青禾取黃黑, 黃禾取黑白, 黑禾取白青
# Total volume of the mixture is 1 dou (實滿斗)

# Coefficients for the equations
# Each row corresponds to the equation for one type of grain
# Columns correspond to the coefficients of 白禾, 青禾, 黃禾, 黑禾, and the total volume
coefficients = [
    [1, -1, -1, 0, 0],  # White grain equation
    [0, 1, -1, -1, 0],  # Green grain equation
    [-1, 0, 1, -1, 0],  # Yellow grain equation
    [-1, -1, 0, 1, 1],  # Black grain equation (total volume = 1 dou)
]

# Initialize variables for the solution
白禾 = 青禾 = 黃禾 = 黑禾 = 0

# Fangcheng method (Gaussian elimination)
# Step 1: Forward elimination
for i in range(4):
    # Normalize the pivot row
    pivot = coefficients[i][i]
    for j in range(5):
        coefficients[i][j] = Fraction(coefficients[i][j], pivot)
    
    # Eliminate the current variable from subsequent rows
    for k in range(i + 1, 4):
        factor = coefficients[k][i]
        for j in range(5):
            coefficients[k][j] -= factor * coefficients[i][j]

# Step 2: Back substitution
solutions = [0, 0, 0, 0]
for i in range(3, -1, -1):
    solutions[i] = coefficients[i][4]
    for j in range(i + 1, 4):
        solutions[i] -= coefficients[i][j] * solutions[j]

# Assign solutions to variables
白禾, 青禾, 黃禾, 黑禾 = solutions

# Output the results
a, b = 白禾, 白禾
c, d = 青禾, 青禾
e, f = 黃禾, 黃禾
g, h = 黑禾, 黑禾

print(f"白禾 {a}步 實 {b}斗")
print(f"青禾 {c}步 實 {d}斗")
print(f"黃禾 {e}步 實 {f}斗")
print(f"黑禾 {g}步 實 {h}斗")


"""


This code uses the **Fangcheng method** (similar to Gaussian elimination) to solve the system of linear equations. Each coefficient corresponds to the relationships described in the problem, and the solution gives the number of steps and the volume of each type of grain.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: -3/5
Variable 'b' has wrong value. Expected: 11/37, Actual: -3/5
Variable 'c' has wrong value. Expected: 1, Actual: -1/5
Variable 'd' has wrong value. Expected: 28/111, Actual: -1/5
Variable 'e' has wrong value. Expected: 1, Actual: -2/5
Variable 'f' has wrong value. Expected: 17/111, Actual: -2/5
Variable 'g' has wrong value. Expected: 1, Actual: 1/5
Variable 'h' has wrong value. Expected: 10/111, Actual: 1/5"""
