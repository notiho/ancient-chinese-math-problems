"""
今有弦五尺，句三尺，問︰為股幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
To solve this problem, we are given the hypotenuse (弦) as 5尺 and one leg (句) as 3尺 of a right triangle. We need to calculate the other leg (股) using the Pythagorean theorem.

The Pythagorean theorem states:
\[
\text{弦}^2 = \text{句}^2 + \text{股}^2
\]

Rearranging for 股:
\[
\text{股} = \sqrt{\text{弦}^2 - \text{句}^2}
\]

Here is the Python code to compute 股:


"""


from fractions import Fraction
import math

# Given values
弦 = Fraction(5)  # 5 尺
句 = Fraction(3)  # 3 尺

# Compute 股
股 = math.sqrt(float(弦**2 - 句**2))

# Convert 股 back to Fraction for exact representation
股 = Fraction(股).limit_denominator()

# Result
a = 股  # 股 in 尺


"""


The value of `a` will be the length of 股 in 尺.
"""


"""
"""
