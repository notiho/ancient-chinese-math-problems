"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
This problem is a classic application of the Pythagorean theorem. The given values are:

- 句 (leg1) = 3 尺
- 股 (leg2) = 4 尺

We are tasked to find the hypotenuse (弦), denoted as `a`.

The Pythagorean theorem states that the square of the hypotenuse is equal to the sum of the squares of the other two sides. In Python, we can compute this as follows:


"""


from fractions import Fraction
import math

# Given values
leg1 = Fraction(3)  # 句
leg2 = Fraction(4)  # 股

# Compute the hypotenuse (弦)
a = Fraction(math.sqrt(leg1**2 + leg2**2))

# Result
a  # Hypotenuse in 尺


"""


The value of `a` will be the hypotenuse in 尺.
"""


"""
"""
