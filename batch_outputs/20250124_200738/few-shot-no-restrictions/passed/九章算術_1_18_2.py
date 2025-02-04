"""
今有田廣七分步之四，從五分步之三。問：為田幾何？
乘分術曰：母相乘為法，子相乘為實，實如法而一。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 4/7 bu and a length of 3/5 bu.
Question: how large is the field?

The procedure for multiplying fractions says: Multiply the denominators to obtain the divisor.
Multiply the numerators to obtain the dividend.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* bu.
"""

from fractions import Fraction

# 田廣七分步之四 (4/7 bu)
廣 = Fraction(4, 7)

# 田從五分步之三 (3/5 bu)
從 = Fraction(3, 5)

# 母相乘為法 (denominators multiplied for the divisor)
法 = 廣.denominator * 從.denominator

# 子相乘為實 (numerators multiplied for the dividend)
實 = 廣.numerator * 從.numerator

# 實如法而一 (divide the dividend by the divisor)
a = Fraction(實, 法)

a  # The area of the field in bu.#----- content ends here -----

"""
"""
