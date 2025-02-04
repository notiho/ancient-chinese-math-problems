"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations to determine the values of `a`, `b`, `c`, and `d`, which represent the amounts of grain in each step for white, green, yellow, and black grains, respectively.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations based on the problem description:
# Each grain type takes one step from two other grain types, and the total becomes one full unit (1斗).

# Equation 1: White (a) + Green (b) + Yellow (c) = 1
# Equation 2: Green (b) + Yellow (c) + Black (d) = 1
# Equation 3: Yellow (c) + Black (d) + White (a) = 1
# Equation 4: Black (d) + White (a) + Green (b) = 1

# Solve the system of equations:
# Add all four equations together:
# 3a + 3b + 3c + 3d = 4
# Simplify:
# a + b + c + d = Fraction(4, 3)

# From the first equation: a + b + c = 1
# Subtract the first equation from the sum of all variables:
# d = Fraction(4, 3) - 1
d = Fraction(4, 3) - 1

# Substitute d into the second equation: b + c + d = 1
# b + c + (Fraction(4, 3) - 1) = 1
# b + c = 1 - (Fraction(4, 3) - 1)
# b + c = Fraction(2, 3)

# Substitute b + c into the first equation: a + b + c = 1
# a + Fraction(2, 3) = 1
# a = 1 - Fraction(2, 3)
a = 1 - Fraction(2, 3)

# Substitute a into the fourth equation: d + a + b = 1
# (Fraction(4, 3) - 1) + a + b = 1
# Fraction(4, 3) - 1 + (1 - Fraction(2, 3)) + b = 1
# b = 1 - (Fraction(4, 3) - 1) - (1 - Fraction(2, 3))
# b = Fraction(2, 3)
b = Fraction(2, 3)

# Substitute b into b + c = Fraction(2, 3)
# Fraction(2, 3) + c = Fraction(2, 3)
# c = 0
c = 0

# The final values are:
# a = Fraction(1, 3), b = Fraction(2, 3), c = 0, d = Fraction(1, 3)

# Assign the results to the variables:
a = Fraction(1, 3)
b = Fraction(2, 3)
c = 0
d = Fraction(1, 3)

# The solution is:
# a = 1/3斗, b = 2/3斗, c = 0斗, d = 1/3斗
#----- content ends here -----


"""


This code solves the system of equations and assigns the values of `a`, `b`, `c`, and `d` to the respective variables. The solution is expressed in terms of fractions to ensure accuracy.
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'b' has wrong value. Expected: 28/111, Actual: 2/3
Variable 'c' has wrong value. Expected: 17/111, Actual: 0
Variable 'd' has wrong value. Expected: 10/111, Actual: 1/3"""
