"""
今有圓篅周三丈髙一丈六尺問受粟幾何
術曰置周尺數自相乗以髙數乗之十二而一得積尺以斛法除之即粟數
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much millet can it hold?

The procedure says: Take the number of chi in the circumference, square it, and multiply it by the number of chi in the height.
Divide the result by 12 to obtain the volume in cubic chi.
Then divide by the hu divisor to get the number of hu of millet.

Answer: *a* hu.
"""

from fractions import Fraction

# 周三丈 (convert to chi)
周 = 3 * 10  # 1 zhang = 10 chi

# 髙一丈六尺 (convert to chi)
髙 = 1 * 10 + 6  # 1 zhang = 10 chi

# 置周尺數自相乘
周平方 = 周 * 周

# 以髙數乘之
積尺 = 周平方 * 髙

# 十二而一
積尺 = Fraction(積尺, 12)

# 斛法 (1 hu = 10 cubic chi)
斛法 = 10

# 以斛法除之，即粟數
a = Fraction(積尺, 斛法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 20000/27, Actual: 120"""
