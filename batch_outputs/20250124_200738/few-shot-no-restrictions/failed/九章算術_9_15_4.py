"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
術曰：八步為句，十五步為股，為之求弦。三位并之為法，以句乘股，倍之為實。實如法得徑一步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with one leg (the "ju") measuring 8 bu and the other leg (the "gu") measuring 15 bu.
Question: What is the diameter of the circle that can fit inside the triangle?

The procedure says: 8 bu is the ju, and 15 bu is the gu. To find the hypotenuse (the "xian"), add the three sides together to form the divisor.
Multiply the ju by the gu, double it to form the dividend.
Divide the dividend by the divisor to obtain the diameter.

Answer: the diameter is *a* bu.
"""

from fractions import Fraction

# Given values
句 = 8  # ju (one leg)
股 = 15  # gu (other leg)

# Calculate the hypotenuse (弦)
弦 = (句**2 + 股**2)**0.5

# 三位并之為法 (add the three sides together to form the divisor)
法 = 句 + 股 + 弦

# 以句乘股，倍之為實 (multiply ju by gu, then double it to form the dividend)
實 = 2 * 句 * 股

# 實如法得徑一步 (divide the dividend by the divisor to get the diameter)
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
