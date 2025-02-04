"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
To solve this problem, we translate the ancient Chinese mathematical problem into Python code. The problem describes a system of linear equations where the total volume of grains from different types of rice (white, green, yellow, and black) is equal to one "斗" (a unit of volume). Each type of rice contributes a certain amount to the total volume based on the problem's description.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem description:
# Let a, b, c, d represent the volume of white, green, yellow, and black rice per step, respectively.
# The equations are derived from the problem:
# 1. a + b + c = 1
# 2. b + c + d = 1
# 3. c + d + a = 1
# 4. d + a + b = 1

# Solve the system of equations:
# Add all four equations:
# (a + b + c) + (b + c + d) + (c + d + a) + (d + a + b) = 4
# 3a + 3b + 3c + 3d = 4
# a + b + c + d = 4 / 3

# Substitute a + b + c = 1 into the equation:
# (1) + d = 4 / 3
# d = 4 / 3 - 1
# d = 1 / 3

# Substitute d = 1 / 3 into a + b + c = 1:
# a + b + c = 1
# a + b + c = 1

# Substitute into the other equations to find a, b, c:
# b + c + d = 1
# b + c + 1 / 3 = 1
# b + c = 2 / 3

# c + d + a = 1
# c + 1 / 3 + a = 1
# c + a = 2 / 3

# d + a + b = 1
# 1 / 3 + a + b = 1
# a + b = 2 / 3

# Solve for a, b, c, d:
d = Fraction(1, 3)
a = Fraction(2, 9)
b = Fraction(2, 9)
c = Fraction(2, 9)

# The solution:
print(f"a = {a} 斗")  # White rice per step
print(f"b = {b} 斗")  # Green rice per step
print(f"c = {c} 斗")  # Yellow rice per step
print(f"d = {d} 斗")  # Black rice per step
#----- content ends here -----


"""


### Explanation of the Solution:
1. The problem describes a system of four linear equations.
2. By summing all equations, we find the total sum of all variables.
3. We substitute known values and simplify the equations to solve for each variable.
4. The final solution gives the volume of each type of rice per step in terms of "斗".
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 2/9
Variable 'b' has wrong value. Expected: 28/111, Actual: 2/9
Variable 'c' has wrong value. Expected: 17/111, Actual: 2/9
Variable 'd' has wrong value. Expected: 10/111, Actual: 1/3"""
