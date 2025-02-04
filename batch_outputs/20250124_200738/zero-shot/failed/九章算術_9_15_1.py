"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
術曰：八步為句，十五步為股，為之求弦。三位并之為法，以句乘股，倍之為實。實如法得徑一步。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the hypotenuse (弦) of a right triangle given the lengths of the two legs (句 and 股). The formula for the hypotenuse in a right triangle is derived from the Pythagorean theorem:

\[
弦 = \sqrt{句^2 + 股^2}
\]

The problem states that the lengths of the legs are 8 steps (句) and 15 steps (股). The hypotenuse is then the diameter of the circle (徑). Let's compute this in Python:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
句 = 8  # in steps
股 = 15  # in steps

# Compute the hypotenuse (diameter of the circle)
a = math.sqrt(句**2 + 股**2)

# Convert to Fraction for exact representation
a = Fraction(a).limit_denominator()

# The answer is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the diameter of the circle in steps.
"""


"""
Variable 'a' has wrong value. Expected: 6, Actual: 17"""
