"""
又有田廣五分步之四，從九分步之五，問：為田幾何？
乘分術曰：母相乘為法，子相乘為實，實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 4/5 bu and a length of 5/9 bu.
Question: how large is the field?

The procedure for multiplying fractions says: Multiply the denominators to obtain the divisor.
Multiply the numerators to obtain the dividend.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* bu².
"""

from fractions import Fraction

# 田廣五分步之四 (4/5 bu)
廣 = Fraction(4, 5)

# 從九分步之五 (5/9 bu)
從 = Fraction(5, 9)

# 母相乘為法 (denominators multiplied for the divisor)
法 = 廣.denominator * 從.denominator

# 子相乘為實 (numerators multiplied for the dividend)
實 = 廣.numerator * 從.numerator

# 實如法而一 (divide the dividend by the divisor)
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
