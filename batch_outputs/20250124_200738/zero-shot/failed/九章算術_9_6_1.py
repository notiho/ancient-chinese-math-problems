"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
distance_from_base = Fraction(8)  # 去本 (distance from the base in 尺)
height_above_ground = Fraction(3)  # 委地 (height above the ground in 尺)

# Calculation
a = (distance_from_base**2 + height_above_ground**2)**Fraction(1, 2)  # 索長 (length of the rope in 尺)

# Convert to 丈 (1 丈 = 10 尺)
a = a / 10

# The result is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the length of the rope in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 73/60, Actual: 0.854400374531753"""
