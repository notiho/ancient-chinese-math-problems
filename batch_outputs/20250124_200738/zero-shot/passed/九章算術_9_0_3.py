"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
This problem is a classic example of the Pythagorean theorem in ancient Chinese mathematics. The problem involves finding the hypotenuse (弦) of a right triangle when the two legs (句 and 股) are given.

Here is the Python code to compute the value of `a` (the hypotenuse):


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
句 = Fraction(3)  # 句 (one leg of the triangle) in 尺
股 = Fraction(4)  # 股 (the other leg of the triangle) in 尺

# Compute the hypotenuse (弦)
a = Fraction(math.sqrt(句**2 + 股**2))

# Result
a  # Hypotenuse in 尺
#----- content ends here -----


"""


The variable `a` will contain the value of the hypotenuse in 尺.
"""


"""
"""
