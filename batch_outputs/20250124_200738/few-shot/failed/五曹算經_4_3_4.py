"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
術曰：列九百斛以二斗五升乘之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 900 hu of millet, and each hu is increased by 2 dou and 5 sheng.
Question: how much is the total increase?

The procedure says: Place the 900 hu and multiply it by 2 dou and 5 sheng to obtain the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟九百斛
粟 = 900

# 斛别加二斗五升
加量 = 2 + Fraction(5, 10)  # 2斗5升 = 2 + 5/10斗

# 列九百斛以二斗五升乘之即得
總加量 = 粟 * 加量

# Convert the result back to hu
a = 總加量#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 225, Actual: 2250"""
