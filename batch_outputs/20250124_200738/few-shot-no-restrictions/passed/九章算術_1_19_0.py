"""
又有田廣九分步之七，從十一分步之九。問：為田幾何？
乘分術曰：母相乘為法，子相乘為實，實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 7/9 bu and a length of 9/11 bu.
Question: how large is the field?

The procedure for multiplying fractions says: Multiply the denominators (the "mothers") to obtain the divisor.
Multiply the numerators (the "sons") to obtain the dividend.
Divide the dividend by the divisor to obtain the result.

Answer: *a* bu².
"""

from fractions import Fraction

# 田廣九分步之七 (width = 7/9 bu)
廣 = Fraction(7, 9)

# 從十一分步之九 (length = 9/11 bu)
從 = Fraction(9, 11)

# 母相乘為法 (denominators multiplied for divisor)
法 = 廣.denominator * 從.denominator

# 子相乘為實 (numerators multiplied for dividend)
實 = 廣.numerator * 從.numerator

# 實如法而一 (divide dividend by divisor)
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
