"""
今有股四尺，弦五尺，問︰為句幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
To solve this problem, we are given the length of the "股" (leg) as 4 尺 and the "弦" (hypotenuse) as 5 尺. We are tasked to find the length of the "句" (the other leg), denoted as `a`.

The problem uses the Pythagorean theorem, which states:
\[ \text{弦}^2 = \text{句}^2 + \text{股}^2 \]

From this, we can solve for the unknown "句":
\[ \text{句}^2 = \text{弦}^2 - \text{股}^2 \]
\[ \text{句} = \sqrt{\text{弦}^2 - \text{股}^2} \]

Here is the Python code to compute the value of `a`:


"""


from fractions import Fraction
import math

# Given values
股 = Fraction(4)  # 股 = 4 尺
弦 = Fraction(5)  # 弦 = 5 尺

# Compute 句 (a)
a = math.sqrt(float(弦**2 - 股**2))  # 句 = sqrt(弦^2 - 股^2)

# Convert back to Fraction for exact representation
a = Fraction(a).limit_denominator()

# The value of a is now stored in the variable `a`


"""


The value of `a` will be the length of the "句" in 尺.
"""


"""
"""
