"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 900 hu of millet. Each hu is increased by 2 dou and 5 sheng.
Question: how much is the total increase?

Answer: *a* hu.
"""

from fractions import Fraction

# 粟九百斛
粟 = 900

# 每斛增加 2斗5升 (1斗 = 10升)
增加量 = 2 + Fraction(5, 10)  # Convert 5升 to 0.5斗

# 總增加量
a = 粟 * 增加量  # Total increase in hu

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 225, Actual: 2250"""
