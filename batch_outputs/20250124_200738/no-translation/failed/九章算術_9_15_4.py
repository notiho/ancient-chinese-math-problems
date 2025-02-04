"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
術曰：八步為句，十五步為股，為之求弦。三位并之為法，以句乘股，倍之為實。實如法得徑一步。
荅曰： a步 。
"""

#----- content starts here -----

# 句八步
句 = 8

# 股十五步
股 = 15

# 三位并之為法
法 = 句 + 股 + (句**2 + 股**2)**0.5  # 弦為直角三角形的斜邊

# 以句乘股，倍之為實
實 = 2 * (句 * 股)

# 實如法得徑一步
a = Fraction(實, 法)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
