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

# Let the number of cars be "a" and the number of people be "b".

# Equation 1: 3 people per car, 2 cars empty
# Total cars = a
# Total people = b
# Cars used = b / 3
# Empty cars = a - b / 3 = 2
# Equation: a - b / 3 = 2

# Equation 2: 2 people per car, 9 people walking
# Total cars = a
# Total people = b
# Cars used = (b - 9) / 2
# Equation: a = (b - 9) / 2

# Solve the system of equations:
# From Equation 2: a = (b - 9) / 2
# Substitute into Equation 1: (b - 9) / 2 - b / 3 = 2

# Solve for b:
# Multiply through by 6 to eliminate fractions:
# 3(b - 9) - 2b = 12
# 3b - 27 - 2b = 12
# b = 39

# Solve for a using Equation 2:
# a = (b - 9) / 2
# a = (39 - 9) / 2
# a = 30 / 2
# a = 15

# Final values:
a = Fraction(15)  # Number of cars
b = Fraction(39)  # Number of people
#----- content ends here -----


"""


The solution is:
- `a` (number of cars) = 15
- `b` (number of people) = 39
"""


"""
"""
