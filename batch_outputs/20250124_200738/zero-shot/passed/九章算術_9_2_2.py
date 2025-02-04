"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
To solve this problem, we are given the length of the hypotenuse (弦, 5尺) and one leg (股, 4尺) of a right triangle. We are tasked with finding the length of the other leg (句), which is represented by "a". The solution uses the Pythagorean theorem.

The Pythagorean theorem states:
\[
\text{弦}^2 = \text{句}^2 + \text{股}^2
\]

Rearranging to solve for 句:
\[
\text{句}^2 = \text{弦}^2 - \text{股}^2
\]

Taking the square root:
\[
\text{句} = \sqrt{\text{弦}^2 - \text{股}^2}
\]

Here is the Python code to compute the value of "a":


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
股 = Fraction(4)  # 股 is 4 尺
弦 = Fraction(5)  # 弦 is 5 尺

# Compute 句 (a)
a = math.sqrt(float(弦**2 - 股**2))  # Using the Pythagorean theorem

# Convert back to Fraction if needed
a = Fraction(a).limit_denominator()

# a is the length of 句 in 尺
#----- content ends here -----


"""


The value of "a" will be the length of the other leg (句) in 尺.
"""


"""
"""
