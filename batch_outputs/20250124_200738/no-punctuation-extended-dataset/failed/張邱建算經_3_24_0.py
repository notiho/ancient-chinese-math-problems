"""
今有粟二百五十斛委注平地下周五大四尺問高幾何
術曰置粟積尺以三十六乘之為實以下周自乘為法實如法得一
答曰 a尺
"""

#----- content starts here -----
"""
Suppose there are 250 hu of millet, poured evenly onto the ground. The circumference of the base is 5 da 4 chi.
Question: what is the height?

The procedure says: Place the volume of millet in cubic chi. Multiply it by 36, obtaining the dividend.
Take the circumference of the base, square it, obtaining the divisor.
Divide the dividend by the divisor, obtaining the height.

Answer: *a* chi.
"""

# 粟二百五十斛
粟 = 250

# 1 斛 = 10 斗, 1 斗 = 10 升, 1 升 = 1 立方尺
粟積尺 = 250 * 10 * 10  # Convert hu to cubic chi

# 以下周五大四尺
周 = 5 * 10 + 4  # Convert 5 da 4 chi to chi

# 置粟積尺以三十六乘之，為實
實 = 36 * 粟積尺

# 以下周自乘，為法
法 = 周 * 周

# 實如法得一
a = Fraction(實, 法)  # Height in chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5, Actual: 25000/81"""
