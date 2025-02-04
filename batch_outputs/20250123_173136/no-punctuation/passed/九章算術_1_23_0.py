"""
又有田廣十八步七分步之五從二十三步十一分步之六問為田幾何
大廣田術曰分母各乘其全分子從之相乘為實分母相乘為法實如法而一
荅曰 a畝 
"""

"""
Suppose there is a field with a width of 18 bu and 5/7 bu, and a length of 23 bu and 6/11 bu.
Question: how large is the field?

The procedure for large rectangular fields says: Multiply the denominators of the fractions by their respective whole numbers.
Add the numerators to them, and multiply these results together to obtain the dividend.
Multiply the denominators together to obtain the divisor.
Divide the dividend by the divisor, and then divide by 240 (the mu divisor) to obtain the result.

The answer says: *a* mu.
"""

from fractions import Fraction

# 廣十八步七分步之五
廣 = 18 + Fraction(5, 7)

# 從二十三步十一分步之六
從 = 23 + Fraction(6, 11)

# 分母各乘其全，分子從之相乘為實
實 = 廣 * 從

# 分母相乘為法
法 = 240  # 畝法

# 實如法而一
a = Fraction(實, 法)
"""
"""
