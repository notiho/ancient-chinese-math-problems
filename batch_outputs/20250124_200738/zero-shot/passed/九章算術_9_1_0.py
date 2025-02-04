"""
今有弦五尺，句三尺，問︰為股幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
This problem involves a right triangle where the hypotenuse (弦) is 5尺, one leg (句) is 3尺, and we are solving for the other leg (股). This is based on the Pythagorean theorem.

Here is the Python code to compute the value of `a` (股):


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
hypotenuse = Fraction(5)  # 弦 (5尺)
leg1 = Fraction(3)        # 句 (3尺)

# Compute 股 (a)
a_squared = hypotenuse**2 - leg1**2
a = Fraction(math.sqrt(a_squared))

# Result
a  # 股 (a in 尺)
#----- content ends here -----


"""


The value of `a` will be computed in 尺.
"""


"""
"""
