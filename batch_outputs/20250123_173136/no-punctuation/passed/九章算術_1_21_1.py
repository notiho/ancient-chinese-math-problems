"""
今有田廣三步三分步之一從五步五分步之二問為田幾何
大廣田術曰分母各乘其全分子從之相乘為實分母相乘為法實如法而一
荅曰 a步 
"""

"""
Suppose there is a field with a width of 3 bu and 1/3 bu, and a length of 5 bu and 2/5 bu.
Question: how large of a field does it make?

The procedure for rectangular fields says: Multiply each denominator by its whole part, and take the numerator along with it.
Multiply these together to obtain the dividend.
Multiply the denominators together to obtain the divisor.
Divide the dividend by the divisor, obtaining the result.

The answer says: *a* bu.
"""

from fractions import Fraction

# 田廣三步三分步之一
廣 = 3 + Fraction(1, 3)

# 從五步五分步之二
從 = 5 + Fraction(2, 5)

# 分母各乘其全，分子從之相乘為實
實 = 廣 * 從

# 分母相乘為法
法 = 1  # Since both are already fractions, their denominators are already accounted for.

# 實如法而一
a = 實  # Result is already in Fraction form.
"""
"""
