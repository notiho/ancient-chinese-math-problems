"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：白禾 a步 實 b斗 ，青禾 c步 實 d斗 ，黃禾 e步 實 f斗 ，黑禾 g步 實 h斗 。
"""

"""
This problem involves solving a system of linear equations using ancient Chinese methods, specifically the "方程術" (method of solving simultaneous equations). The problem describes a situation where four types of grain (white, green, yellow, and black) are exchanged in specific amounts, and the total volume of grain is exactly one dou. The goal is to find the actual volume of each type of grain per step.

To solve this, we will translate the ancient procedure into Python code step by step.


"""


from fractions import Fraction

# Define the coefficients of the equations based on the problem description
# White grain (白禾), Green grain (青禾), Yellow grain (黃禾), Black grain (黑禾)
# Each row corresponds to one equation
coefficients = [
    [1, 1, 1, 0],  # White takes 1 step of Green and Yellow
    [0, 1, 1, 1],  # Green takes 1 step of Yellow and Black
    [1, 0, 1, 1],  # Yellow takes 1 step of Black and White
    [1, 1, 0, 1],  # Black takes 1 step of White and Green
]

# Define the total volume (1 dou) as the right-hand side of the equations
total_volume = [1, 1, 1, 1]

# Step 1: Initialize variables for the solution
white = Fraction(0)
green = Fraction(0)
yellow = Fraction(0)
black = Fraction(0)

# Step 2: Solve the system of equations using the ancient method
# Normalize the first row
factor = coefficients[0][0]
coefficients[0] = [x / factor for x in coefficients[0]]
total_volume[0] /= factor

# Eliminate the first variable from the other rows
for i in range(1, 4):
    factor = coefficients[i][0]
    coefficients[i] = [coefficients[i][j] - factor * coefficients[0][j] for j in range(4)]
    total_volume[i] -= factor * total_volume[0]

# Normalize the second row
factor = coefficients[1][1]
coefficients[1] = [x / factor for x in coefficients[1]]
total_volume[1] /= factor

# Eliminate the second variable from the other rows
for i in [0, 2, 3]:
    factor = coefficients[i][1]
    coefficients[i] = [coefficients[i][j] - factor * coefficients[1][j] for j in range(4)]
    total_volume[i] -= factor * total_volume[1]

# Normalize the third row
factor = coefficients[2][2]
coefficients[2] = [x / factor for x in coefficients[2]]
total_volume[2] /= factor

# Eliminate the third variable from the other rows
for i in [0, 1, 3]:
    factor = coefficients[i][2]
    coefficients[i] = [coefficients[i][j] - factor * coefficients[2][j] for j in range(4)]
    total_volume[i] -= factor * total_volume[2]

# Solve for the fourth variable
black = total_volume[3] / coefficients[3][3]

# Back-substitute to solve for the other variables
yellow = total_volume[2] - coefficients[2][3] * black
green = total_volume[1] - coefficients[1][2] * yellow - coefficients[1][3] * black
white = total_volume[0] - coefficients[0][1] * green - coefficients[0][2] * yellow - coefficients[0][3] * black

# Output the results
a, b = 1, white
c, d = 1, green
e, f = 1, yellow
g, h = 1, black

print(f"白禾 {a}步 實 {b}斗")
print(f"青禾 {c}步 實 {d}斗")
print(f"黃禾 {e}步 實 {f}斗")
print(f"黑禾 {g}步 實 {h}斗")


"""
 

This code follows the ancient procedure step by step to solve the system of equations and determine the volume of each type of grain. Each variable (white, green, yellow, black) represents the volume of grain per step.
"""


"""
Variable 'b' has wrong value. Expected: 11/37, Actual: 0.3333333333333333
Variable 'd' has wrong value. Expected: 28/111, Actual: 0.3333333333333333
Variable 'f' has wrong value. Expected: 17/111, Actual: 0.33333333333333337
Variable 'h' has wrong value. Expected: 10/111, Actual: 0.3333333333333333"""
