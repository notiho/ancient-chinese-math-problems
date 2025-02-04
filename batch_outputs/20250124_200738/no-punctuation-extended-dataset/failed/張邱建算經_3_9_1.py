"""
今有窖上方八尺下方一丈二尺受粟九百三十八斛八十一分斛之二十二問深幾何
術曰置粟積尺以三乘之為實上下方相乘併又各自乘併以為法實如法而一
答曰 a丈
"""

#----- content starts here -----
"""
Suppose there is a granary with an upper square side of 8 chi and a lower square side of 12 chi. 
It holds 938 hu and 22/81 of a hu of millet.
Question: how deep is the granary?

The procedure says: Place the millet volume in chi and multiply it by 3, obtaining the dividend.
Multiply the upper and lower square sides with each other and add them. 
Then, square each of them and add these as well, obtaining the divisor.
Divide the dividend by the divisor, obtaining the depth.

Answer: *a* zhang.
"""

from fractions import Fraction

# 上方八尺
上方 = 8

# 下方一丈二尺 (convert to chi: 1 zhang = 10 chi)
下方 = 12

# 粟九百三十八斛八十一分斛之二十二 (convert to a single fraction)
粟 = 938 + Fraction(22, 81)

# 置粟積尺以三乘之，為實
實 = 3 * 粟

# 上下方相乘併
上下相乘 = 上方 * 下方

# 又各自乘併
各自平方 = 上方**2 + 下方**2

# 以為法
法 = 上下相乘 + 各自平方

# 實如法而一
深 = Fraction(實, 法)

# Convert depth to zhang (1 zhang = 10 chi)
a = 深 / 10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3/2, Actual: 25/27"""
