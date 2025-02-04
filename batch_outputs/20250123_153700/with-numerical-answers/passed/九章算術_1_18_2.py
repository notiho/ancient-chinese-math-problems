"""
今有田廣七分步之四，從五分步之三。問：為田幾何？
乘分術曰：母相乘為法，子相乘為實，實如法而一。
荅曰： a(=12/35)步 。
"""

"""
Suppose there is a field with a width of 4/7 bu and a length of 3/5 bu.
Question: how large is the field?

The procedure for multiplying fractions says: Multiply the denominators to obtain the divisor.
Multiply the numerators to obtain the dividend.
Divide the dividend by the divisor to obtain the result.

Answer: *a*(=12/35) bu².
"""

from fractions import Fraction

# 田廣七分步之四
廣 = Fraction(4, 7)

# 從五分步之三
從 = Fraction(3, 5)

# 母相乘為法
法 = 廣.denominator * 從.denominator

# 子相乘為實
實 = 廣.numerator * 從.numerator

# 實如法而一
a = Fraction(實, 法)  # 12/35
"""
"""
