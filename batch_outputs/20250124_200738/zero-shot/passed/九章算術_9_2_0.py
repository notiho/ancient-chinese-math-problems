"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
This problem involves a right triangle where the lengths of the hypotenuse (弦) and one leg (股) are given, and the length of the other leg (句) is to be determined. The solution uses the Pythagorean theorem.

Here is the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
股 = Fraction(4)  # 股 (one leg) = 4 尺
弦 = Fraction(5)  # 弦 (hypotenuse) = 5 尺

# Compute 句 (the other leg)
a = (弦**2 - 股**2)**0.5  # Pythagorean theorem: 弦^2 = 股^2 + 句^2

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` is the length of the other leg (句) in 尺.
"""


"""
"""
