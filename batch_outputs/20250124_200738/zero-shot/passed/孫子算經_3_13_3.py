"""
今有三人共車，二車空；二人共車，九人步。問：人與車各幾何？
術曰：置二人以三乘之，得六，加步者九人，得車一十五，欲知人者，以二乘車，加九人即得。
答曰： a 車， b人 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Let the number of cars be 'a' and the number of people be 'b'.

# Equation 1: 3 people share a car, 2 cars are empty
# Total cars = (b / 3) + 2
# a = (b / 3) + 2

# Equation 2: 2 people share a car, 9 people walk
# Total cars = (b - 9) / 2
# a = (b - 9) / 2

# Solve the two equations for 'a' and 'b'
# (b / 3) + 2 = (b - 9) / 2

# Multiply through by 6 to eliminate fractions:
# 6 * (b / 3) + 6 * 2 = 6 * ((b - 9) / 2)
# 2b + 12 = 3b - 27

# Simplify:
# 12 + 27 = 3b - 2b
# b = 39

# Substitute b = 39 into one of the original equations to find 'a':
# a = (b / 3) + 2
# a = (39 / 3) + 2
# a = 13 + 2
# a = 15

# Final values:
a = Fraction(15)  # Number of cars
b = Fraction(39)  # Number of people
#----- content ends here -----


"""


The solution is:
- `a = 15` cars
- `b = 39` people
"""


"""
"""
