"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
To solve this problem, we are given a right triangle where the length of the hypotenuse (弦) is 5尺, and the length of one leg (股) is 4尺. We are tasked to find the length of the other leg (句), denoted as "a".

Using the Pythagorean theorem:
\[
\text{弦}^2 = \text{句}^2 + \text{股}^2
\]
We can solve for 句:
\[
\text{句}^2 = \text{弦}^2 - \text{股}^2
\]
\[
\text{句} = \sqrt{\text{弦}^2 - \text{股}^2}
\]

Here is the Python code to compute the value of "a":


"""


from fractions import Fraction
import math

# Given values
股 = Fraction(4)  # 股 = 4尺
弦 = Fraction(5)  # 弦 = 5尺

# Calculate 句 (a)
a = math.sqrt(float(弦**2 - 股**2))

# Convert back to Fraction if needed
a = Fraction(a).limit_denominator()

# The solution is stored in variable "a"


"""


The value of "a" will represent the length of 句 in 尺.
"""


"""
"""
