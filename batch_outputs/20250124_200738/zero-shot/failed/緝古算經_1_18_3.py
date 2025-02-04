"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
術曰：冪自乘，為實。句自乘，為方法，從。開方除之，所得又開方，即股
答曰：股 a 。
"""

"""
To solve the problem, let's translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
mian = 726  # 冪 (hypotenuse squared)
ju = Fraction(7, 10)  # 句 (base)

# Step 1: Calculate the square of the base (句自乘)
ju_squared = ju ** 2

# Step 2: Subtract the square of the base from the hypotenuse squared (冪自乘 - 句自乘)
shi = mian - ju_squared  # 實 (result)

# Step 3: Take the square root of the result (開方)
gu = math.sqrt(shi)  # 股 (perpendicular)

# Assign the result to variable 'a'
a = gu

# Output the result
a
#----- content ends here -----


"""


Here, `a` represents the length of the perpendicular side (股). The calculation uses the given hypotenuse squared (冪) and base (句) to find the perpendicular side (股).
"""


"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 26.935292833010003"""
