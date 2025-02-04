"""
今有田廣七分步之四從五分步之三問為田幾何
乘分術曰母相乘為法子相乘為實實如法而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 4/7 bu and a length of 3/5 bu.
Question: how large of a field does it make?

The procedure for multiplying fractions says: Multiply the denominators (the "mothers") to obtain the divisor.
Multiply the numerators (the "sons") to obtain the dividend.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* bu.
"""

# 田廣七分步之四
廣 = Fraction(4, 7)

# 從五分步之三
從 = Fraction(3, 5)

# 母相乘為法
法 = 廣.denominator * 從.denominator

# 子相乘為實
實 = 廣.numerator * 從.numerator

# 實如法而一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
