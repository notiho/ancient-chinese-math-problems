"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
術曰：列九百斛以二斗五升乘之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 900 hu of millet, and each hu is increased by 2 dou and 5 sheng.
Question: how much is the total increase?

The procedure says: Place 900 hu and multiply it by 2 dou and 5 sheng to obtain the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟九百斛
粟 = 900  # in hu

# 每斛加二斗五升
# Convert 2 dou 5 sheng to hu
# 1 hu = 10 dou, 1 dou = 10 sheng
加量 = 2 + Fraction(5, 10)  # in hu

# 以九百斛乘加量
總加量 = 粟 * 加量

# 答案
a = 總加量
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 225, Actual: 2250"""
