"""
今有圓材徑頭二尺一寸欲以為方問各㡬何
術曰置徑尺寸數以五乗之為實以七為法實如法而一
答曰 a尺
"""

"""
Suppose there is a cylindrical log with a diameter of 2 chi and 1 cun. 
It is desired to convert it into a square cross-section.
Question: what is the side length of the square?

The procedure says: Place the diameter in chi and cun. Multiply it by itself five times to obtain the dividend. 
Take 7 as the divisor. Divide the dividend by the divisor to obtain the side length.

Answer: *a* chi.
"""

from fractions import Fraction

# 圓材徑頭二尺一寸
徑 = 2 + Fraction(1, 10)  # 2 chi and 1 cun (1 chi = 10 cun)

# 以五乘之為實
實 = 徑**5

# 以七為法
法 = 7

# 實如法而一
a = Fraction(實, 法)  # Side length of the square in chi
"""
Variable 'a' has wrong value. Expected: 3/2, Actual: 583443/100000"""
