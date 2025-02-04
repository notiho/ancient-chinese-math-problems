"""
今有句五步，股十二步。問︰句中容方幾何？
術曰：并句、股為法，句股相乘為實，實如法而一，得方一步。
荅曰：方 a步 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 5 bu and a height (leg) of 12 bu.
Question: How many square bu can fit in the square inscribed in the triangle?

The procedure says: Add the base and height together to form the divisor.
Multiply the base and height together to form the dividend.
Divide the dividend by the divisor to obtain the side length of the square.

Answer: The side length of the square is *a* bu.
"""

from fractions import Fraction

# 句五步 (base of the triangle)
句 = 5

# 股十二步 (height of the triangle)
股 = 12

# 并句、股為法 (add base and height to form the divisor)
法 = 句 + 股

# 句股相乘為實 (multiply base and height to form the dividend)
實 = 句 * 股

# 實如法而一，得方一步 (divide the dividend by the divisor to get the side length of the square)
a = Fraction(實, 法)

a  # The side length of the square in bu#----- content ends here -----

"""
"""
