"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Define the system of equations based on the problem description:
# Let a, b, c, d represent the amount of white, green, yellow, and black grains per step, respectively.
# The equations are derived from the problem:
# 1. a + b + c = 1
# 2. b + c + d = 1
# 3. c + d + a = 1
# 4. d + a + b = 1

# Solve the system of equations:
# Add all four equations:
# (a + b + c) + (b + c + d) + (c + d + a) + (d + a + b) = 4
# 3a + 3b + 3c + 3d = 4
# a + b + c + d = Fraction(4, 3)

# Subtract each equation from the sum to find individual values:
# a = (a + b + c + d) - (b + c + d)
# b = (a + b + c + d) - (c + d + a)
# c = (a + b + c + d) - (d + a + b)
# d = (a + b + c + d) - (a + b + c)

# Compute the values:
total = Fraction(4, 3)
a = total - 1  # a = (4/3) - 1
b = total - 1  # b = (4/3) - 1
c = total - 1  # c = (4/3) - 1
d = total - 1  # d = (4/3) - 1

# Print the results:
a, b, c, d
#----- content ends here -----


"""


This code computes the values of `a`, `b`, `c`, and `d` using the `Fraction` class to ensure precision with fractions. The results are stored in the variables `a`, `b`, `c`, and `d`.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'b' has wrong value. Expected: 28/111, Actual: 1/3
Variable 'c' has wrong value. Expected: 17/111, Actual: 1/3
Variable 'd' has wrong value. Expected: 10/111, Actual: 1/3"""
