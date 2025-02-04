"""
又有田廣九分步之七從十一分步之九問為田幾何
乘分術曰母相乘為法子相乘為實實如法而一
荅曰 a步 
"""

"""
Suppose there is a field with a width of 7/9 bu and a length of 9/11 bu.
Question: how large of a field does it make?

The procedure for multiplying fractions says: Multiply the denominators to obtain the divisor.
Multiply the numerators to obtain the dividend.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* bu.
"""

# 廣九分步之七
廣 = Fraction(7, 9)

# 從十一分步之九
從 = Fraction(9, 11)

# 母相乘為法
法 = 廣.denominator * 從.denominator

# 子相乘為實
實 = 廣.numerator * 從.numerator

# 實如法而一
a = Fraction(實, 法)
"""
"""
