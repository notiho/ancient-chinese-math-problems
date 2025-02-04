"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
This is a classic system of linear equations problem. Let's solve it step by step in Python using the `Fraction` class to ensure exact arithmetic.

The problem can be represented as:

1. \( 3x + 2y + z = 39 \)
2. \( 2x + 3y + z = 34 \)
3. \( x + 2y + 3z = 26 \)

Where:
- \( x \) is the amount of dou (斗) for one bundle of upper-grade grain (上禾),
- \( y \) is the amount of dou (斗) for one bundle of middle-grade grain (中禾),
- \( z \) is the amount of dou (斗) for one bundle of lower-grade grain (下禾).

We solve this system of equations step by step.


"""


from fractions import Fraction

# Coefficients of the equations
# 3x + 2y + z = 39
# 2x + 3y + z = 34
# x + 2y + 3z = 26

# Step 1: Eliminate z from the first two equations
a1, b1, c1, d1 = 3, 2, 1, 39  # Equation 1: 3x + 2y + z = 39
a2, b2, c2, d2 = 2, 3, 1, 34  # Equation 2: 2x + 3y + z = 34
a3, b3, c3, d3 = 1, 2, 3, 26  # Equation 3: x + 2y + 3z = 26

# Eliminate z from Equation 1 and Equation 2
multiplier1 = c2
multiplier2 = c1
new_a1 = a1 * multiplier1 - a2 * multiplier2
new_b1 = b1 * multiplier1 - b2 * multiplier2
new_d1 = d1 * multiplier1 - d2 * multiplier2

# Resulting equation: new_a1 * x + new_b1 * y = new_d1
# -1x - 1y = -5
# Simplify:
new_a1, new_b1, new_d1 = -1, -1, -5

# Eliminate z from Equation 2 and Equation 3
multiplier3 = c3
multiplier4 = c2
new_a2 = a2 * multiplier3 - a3 * multiplier4
new_b2 = b2 * multiplier3 - b3 * multiplier4
new_d2 = d2 * multiplier3 - d3 * multiplier4

# Resulting equation: new_a2 * x + new_b2 * y = new_d2
# 5x + 3y = 22
# Simplify:
new_a2, new_b2, new_d2 = 5, 3, 22

# Step 2: Solve for x and y using the two new equations
# Equation 1: -x - y = -5
# Equation 2: 5x + 3y = 22

# Multiply Equation 1 by 3 to align coefficients of y
multiplier5 = 3
final_a1 = new_a1 * multiplier5
final_b1 = new_b1 * multiplier5
final_d1 = new_d1 * multiplier5

# Resulting equation: -3x - 3y = -15
# Equation 2 remains: 5x + 3y = 22

# Add the two equations to eliminate y
final_a2 = new_a2
final_b2 = new_b2
final_d2 = new_d2

x = Fraction(final_d1 + final_d2, final_a1 + final_a2)

# Substitute x back into one of the equations to solve for y
y = Fraction(-new_a1 * x - new_d1, new_b1)

# Step 3: Solve for z using one of the original equations
# Use Equation 1: 3x + 2y + z = 39
z = Fraction(d1 - a1 * x - b1 * y, c1)

# Results
a = x  # 上禾一秉
b = y  # 中禾一秉
c = z  # 下禾一秉

print(f"上禾一秉: {a}斗, 中禾一秉: {b}斗, 下禾一秉: {c}斗")


"""


### Explanation of Results:
- \( a \): The amount of dou (斗) for one bundle of upper-grade grain (上禾).
- \( b \): The amount of dou (斗) for one bundle of middle-grade grain (中禾).
- \( c \): The amount of dou (斗) for one bundle of lower-grade grain (下禾).

This Python code solves the system of equations step by step using exact arithmetic with the `Fraction` class.
"""


"""
Variable 'a' has wrong value. Expected: 37/4, Actual: 7/2
Variable 'b' has wrong value. Expected: 17/4, Actual: -17/2
Variable 'c' has wrong value. Expected: 11/4, Actual: 91/2"""
