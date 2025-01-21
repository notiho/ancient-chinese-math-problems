"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
This problem involves solving a system of linear equations to determine the yield of each type of grain (upper, middle, and lower) per bundle. Let's translate this into Python code.


"""


from fractions import Fraction

# Define the equations based on the problem statement
# Let x = yield of upper grain per bundle (in dou)
# Let y = yield of middle grain per bundle (in dou)
# Let z = yield of lower grain per bundle (in dou)

# Equation 1: 3x + 2y + 1z = 39
# Equation 2: 2x + 3y + 1z = 34
# Equation 3: 1x + 2y + 3z = 26

# Solve the system of equations using substitution or elimination

# Step 1: Eliminate z from the first two equations
# Multiply Equation 1 by 1 and Equation 2 by -1, then add them
# (3x + 2y + z) - (2x + 3y + z) = 39 - 34
# x - y = 5  --> Equation 4

# Step 2: Eliminate z from the first and third equations
# Multiply Equation 1 by 3 and Equation 3 by -1, then add them
# (9x + 6y + 3z) - (1x + 2y + 3z) = 117 - 26
# 8x + 4y = 91  --> Equation 5

# Step 3: Solve for x and y using Equation 4 and Equation 5
# From Equation 4: y = x - 5
# Substitute y = x - 5 into Equation 5:
# 8x + 4(x - 5) = 91
# 8x + 4x - 20 = 91
# 12x = 111
x = Fraction(111, 12)

# Solve for y using Equation 4: y = x - 5
y = x - 5

# Solve for z using Equation 1: 3x + 2y + z = 39
z = 39 - (3 * x + 2 * y)

# Output the results
a, b = 1, x  # Upper grain yield per bundle
c, d = 1, y  # Middle grain yield per bundle
e, f = 1, z  # Lower grain yield per bundle

print(f"上禾 {a}秉 ， {b}斗 ，中禾 {c}秉 ， {d}斗 ，下禾 {e}秉 ， {f}斗 。")


"""


This Python code solves the system of equations step by step and outputs the yield of each type of grain per bundle in terms of fractions (using the `Fraction` class).
"""


"""
"""
