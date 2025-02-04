"""
又有田廣七步四分步之三從十五步九分步之五問為田幾何
大廣田術曰分母各乘其全分子從之相乘為實分母相乘為法實如法而一
荅曰 a步 
"""

"""
Suppose there is a field with a width of 7 bu and 3/4 bu, and a length of 15 bu and 5/9 bu.
Question: how large is the field?

The procedure for large rectangular fields says: Multiply the denominators of the fractions by their whole numbers.
Take the numerators of the fractions and multiply them together as the dividend.
Multiply the denominators together as the divisor.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* bu.
"""

from fractions import Fraction

# 廣七步四分步之三
廣 = 7 + Fraction(3, 4)

# 從十五步九分步之五
從 = 15 + Fraction(5, 9)

# 分母各乘其全，分子從之相乘為實
實 = 廣 * 從

# 實如法而一
a = 實  # The result is already in terms of bu.
"""
"""
