"""
又有田廣十八步、七分步之五，從二十三步、十一分步之六。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a(=4847/2640)畝 。
"""

"""
Suppose there is a field with a width of 18 bu and 5/7 bu, and a length of 23 bu and 6/11 bu.
Question: how large is the field?

The procedure for large rectangular fields says: Multiply each denominator by its whole number, and the numerator follows it. Multiply these together to obtain the dividend. Multiply the denominators together to obtain the divisor. Divide the dividend by the divisor to obtain the result.

The answer says: *a*(=4847/2640) mu.
"""

from fractions import Fraction

# 廣十八步、七分步之五
廣整數 = 18
廣分子 = 5
廣分母 = 7
廣 = 廣整數 + Fraction(廣分子, 廣分母)

# 從二十三步、十一分步之六
從整數 = 23
從分子 = 6
從分母 = 11
從 = 從整數 + Fraction(從分子, 從分母)

# 分母各乘其全，分子從之，相乘為實
實 = 廣 * 從

# 分母相乘為法
畝法 = 240  # 每畝240步
實 = 實 / 畝法

# 實如法而一
a = 實  # 4847/2640

"""
"""
