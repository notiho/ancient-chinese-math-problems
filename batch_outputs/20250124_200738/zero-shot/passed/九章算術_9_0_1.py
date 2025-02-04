"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
This problem is a classic example of the Pythagorean theorem, where the hypotenuse (弦) is calculated given the lengths of the other two sides (句 and 股) of a right triangle.

Here is the Python code to compute the value of the hypotenuse (`a`):


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
句 = Fraction(3)  # 3 尺
股 = Fraction(4)  # 4 尺

# Calculate the hypotenuse (弦)
a = Fraction(math.sqrt(句**2 + 股**2))  # a 尺

# Result
a
#----- content ends here -----


"""


The value of `a` will be the length of the hypotenuse in 尺.
"""


"""
"""
