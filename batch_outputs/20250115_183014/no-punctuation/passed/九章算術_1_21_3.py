"""
今有田廣三步三分步之一從五步五分步之二問為田幾何
大廣田術曰分母各乘其全分子從之相乘為實分母相乘為法實如法而一
荅曰 a步 
"""

"""
Suppose there is a field with a width of 3 bu and 1/3 bu, and a length of 5 bu and 2/5 bu.
Question: how large is the field?

The procedure for rectangular fields says: Multiply the denominators of each fractional part by their respective whole numbers. 
Take the numerators of the fractions and multiply them together to form the dividend.
Multiply the denominators together to form the divisor.
Divide the dividend by the divisor to get the result.

The answer says: *a* bu.
"""

from fractions import Fraction

# 廣三步三分步之一
廣 = 3 + Fraction(1, 3)

# 從五步五分步之二
從 = 5 + Fraction(2, 5)

# 分母各乘其全，分子從之相乘為實
實 = 廣 * 從

# 實如法而一
a = 實  # The result is already in terms of bu.
"""
"""
