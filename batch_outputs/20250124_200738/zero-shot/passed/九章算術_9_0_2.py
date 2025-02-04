"""
今有句三尺，股四尺，問︰為弦幾何？
句股術曰：句股各自乘，并，而開方除之，即弦。又股自乘，以減弦自乘，其餘開方除之，即句。又句自乘，以減弦自乘，其餘開方除之，即股。
荅曰： a尺 。
"""

"""
This is a classic Pythagorean theorem problem. The problem states that the lengths of the two legs of a right triangle are 3 feet (句) and 4 feet (股), and it asks for the length of the hypotenuse (弦). The formula for the hypotenuse is:

\[
\text{弦} = \sqrt{\text{句}^2 + \text{股}^2}
\]

Here is the Python code to compute the value of the hypotenuse:


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Given values
句 = Fraction(3)  # 3 feet
股 = Fraction(4)  # 4 feet

# Compute the hypotenuse
a = Fraction(sqrt(句**2 + 股**2))

# The answer is stored in variable 'a'
#----- content ends here -----


"""


The value of `a` will be the length of the hypotenuse in feet.
"""


"""
"""
