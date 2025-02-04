"""
今有句八步股十五步問句中容圓徑幾何
術曰八步為句十五步為股為之求弦三位并之為法以句乘股倍之為實實如法得徑一步
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 8 bu and a height (leg) of 15 bu.
Question: what is the diameter of the inscribed circle?

The procedure says: Take 8 bu as the base (leg) and 15 bu as the height (leg). 
To find the hypotenuse, add the three sides together to form the divisor.
Multiply the base by the height and double it to form the dividend.
Divide the dividend by the divisor to obtain the diameter.

The answer says: *a* bu.
"""

# 句八步
句 = 8

# 股十五步
股 = 15

# 求弦
弦 = (句**2 + 股**2)**0.5

# 三位并之為法
法 = 句 + 股 + 弦

# 以句乘股倍之為實
實 = 2 * 句 * 股

# 實如法得徑
a = Fraction(實, 法)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
