"""
今有粟二百五十斛委注平地下周五大四尺問高幾何
術曰置粟積尺以三十六乘之為實以下周自乘為法實如法得一
答曰 a尺
"""

"""
Suppose there are 250 hu of millet poured evenly onto the ground, forming a circular base with a circumference of 5 zhang and 4 chi.
Question: what is the height?

The procedure says: Place the millet volume in cubic chi, multiply it by 36 to obtain the dividend.
Take the circumference, square it to obtain the divisor.
Divide the dividend by the divisor to obtain the height.

Answer: *a* chi.
"""

# 粟二百五十斛
粟 = 250

# 1斛 = 10斗, 1斗 = 10升, 1升 = 1立方尺
# Convert 粟 to cubic chi (立方尺)
粟積尺 = 250 * 10 * 10

# 地下周五大四尺 (5丈4尺 = 54尺)
周 = 5 * 10 + 4

# 置粟積尺，以三十六乘之，為實
實 = 粟積尺 * 36

# 以下周自乘，為法
法 = 周 * 周

# 實如法得一
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 5, Actual: 25000/81"""
