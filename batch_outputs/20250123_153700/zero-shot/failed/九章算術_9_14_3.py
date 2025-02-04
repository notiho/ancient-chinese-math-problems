"""
今有句五步，股十二步。問︰句中容方幾何？
術曰：并句、股為法，句股相乘為實，實如法而一，得方一步。
荅曰：方 a步 。
"""

"""
This problem involves solving for the hypotenuse (方, "a") of a right triangle given the lengths of the other two sides (句 and 股). The formula for the hypotenuse is derived from the Pythagorean theorem:

\[
a = \sqrt{句^2 + 股^2}
\]

Here is the Python code to compute the value of \( a \):


"""


from fractions import Fraction
import math

# Given values
句 = Fraction(5)  # 5 steps
股 = Fraction(12)  # 12 steps

# Compute the hypotenuse (方)
a = math.sqrt(float(句**2 + 股**2))

# Convert back to Fraction for consistency
a = Fraction(a).limit_denominator()

# The result is stored in variable 'a'


"""


The value of \( a \) will be the hypotenuse in steps.
"""


"""
Variable 'a' has wrong value. Expected: 60/17, Actual: 13"""
