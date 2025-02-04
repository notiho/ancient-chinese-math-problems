"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
術曰：八步為句，十五步為股，為之求弦。三位并之為法，以句乘股，倍之為實。實如法得徑一步。
荅曰： a(=6)步 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 8 bu and a height (leg) of 15 bu.
Question: what is the diameter of the circle that fits inside the triangle?

The procedure says: 8 bu is the base (leg), and 15 bu is the height (leg). To find the hypotenuse:
Add the three terms together to form the divisor.
Multiply the base by the height, double it to form the dividend.
Divide the dividend by the divisor to obtain the diameter.

Answer: *a*(=6) bu.
"""

# 句八步
句 = 8

# 股十五步
股 = 15

# 三位并之為法
法 = 句 + 股 + (句**2 + 股**2)**0.5

# 以句乘股
實 = 句 * 股

# 倍之為實
實 = 2 * 實

# 實如法得徑一步
a = Fraction(實, 法) # 6#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
