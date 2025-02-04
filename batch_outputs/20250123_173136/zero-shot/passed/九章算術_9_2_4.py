"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
To solve this problem, we are given a right triangle where the length of the "股" (leg) is 4 尺, the "弦" (hypotenuse) is 5 尺, and we are tasked to find the length of the "句" (other leg). Using the Pythagorean theorem, we can calculate the unknown "句".

Here is the Python code:


"""


from fractions import Fraction

# Given values
股 = Fraction(4)  # 股 (leg) in 尺
弦 = Fraction(5)  # 弦 (hypotenuse) in 尺

# Using the Pythagorean theorem to find 句
句 = (弦**2 - 股**2)**0.5  # 句 (other leg) in 尺

# The result
a = 句


"""


The value of `a` will be the length of the "句" in 尺.
"""


"""
"""
