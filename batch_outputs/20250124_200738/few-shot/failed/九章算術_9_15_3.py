"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
術曰：八步為句，十五步為股，為之求弦。三位并之為法，以句乘股，倍之為實。實如法得徑一步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 8 bu and a height (leg) of 15 bu.
Question: what is the diameter of the circle that can fit inside the triangle?

The procedure says: 8 bu is the base (leg), 15 bu is the height (leg). To find the hypotenuse:
Add the three terms (base, height, and hypotenuse) together to form the divisor.
Multiply the base by the height, and double it to form the dividend.
Divide the dividend by the divisor to obtain the diameter of 1 bu.

Answer: *a* bu.
"""

# 句八步
句 = 8

# 股十五步
股 = 15

# 求弦 (using the Pythagorean theorem)
弦 = (句**2 + 股**2)**0.5

# 三位并之為法 (add base, height, and hypotenuse to form the divisor)
法 = 句 + 股 + 弦

# 以句乘股，倍之為實 (multiply base by height, then double it to form the dividend)
實 = 2 * 句 * 股

# 實如法得徑一步 (divide the dividend by the divisor to get the diameter)
a = Fraction(實, 法)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
