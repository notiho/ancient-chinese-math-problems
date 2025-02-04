"""
今有三人共車，二車空；二人共車，九人步。問：人與車各幾何？
術曰：置二人以三乘之，得六，加步者九人，得車一十五，欲知人者，以二乘車，加九人即得。
答曰： a 車， b人 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Let the number of cars be 'a' and the number of people be 'b'.

# Equation 1: 3 people share a car, and 2 cars are empty.
# This means the total number of cars is a, and the total number of people is b.
# So, 3 * (a - 2) = b.

# Equation 2: 2 people share a car, and 9 people are walking.
# This means the total number of cars is a, and the total number of people is b.
# So, 2 * a + 9 = b.

# Solve these equations:
# From Equation 1: b = 3 * (a - 2)
# From Equation 2: b = 2 * a + 9

# Set the two equations for b equal to each other:
# 3 * (a - 2) = 2 * a + 9

# Expand and simplify:
# 3a - 6 = 2a + 9
# a = 15

# Substitute a = 15 into one of the equations for b:
# b = 3 * (15 - 2)
# b = 3 * 13
# b = 39

# Final values:
a = 15  # Number of cars
b = 39  # Number of people
#----- content ends here -----


"""


The solution is:
- `a = 15` cars
- `b = 39` people
"""


"""
"""
