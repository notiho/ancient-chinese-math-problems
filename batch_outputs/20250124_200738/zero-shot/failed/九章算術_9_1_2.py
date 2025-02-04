"""
今有弦五尺，句三尺，問︰為股幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
To solve this problem, we are given the hypotenuse (弦) as 5 尺 and one leg (句) as 3 尺 of a right triangle. We need to calculate the other leg (股). Using the Pythagorean theorem:

\[
\text{弦}^2 = \text{句}^2 + \text{股}^2
\]

Rearranging to solve for 股:

\[
\text{股}^2 = \text{弦}^2 - \text{句}^2
\]

Taking the square root:

\[
\text{股} = \sqrt{\text{弦}^2 - \text{句}^2}
\]

Here is the Python code to compute the value of 股:


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Given values
弦 = Fraction(5)  # 5 尺
句 = Fraction(3)  # 3 尺

# Compute 股
股 = sqrt(float(弦**2 - 句**2))

# 股 is the answer
股
#----- content ends here -----


"""


The value of `股` will be computed in 尺.
"""


"""
Missing variable in output: 'a'"""
