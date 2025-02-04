"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
This problem is a classic example of the Pythagorean theorem. The given problem states that the lengths of the two legs of a right triangle are 3 feet (句) and 4 feet (股), and we are tasked to find the hypotenuse (弦).

Here is the Python code to compute the value of the hypotenuse (弦):


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
句 = Fraction(3)  # 3 feet
股 = Fraction(4)  # 4 feet

# Compute the hypotenuse (弦)
a = Fraction(math.sqrt(句**2 + 股**2))

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will be the length of the hypotenuse in feet.
"""


"""
"""
