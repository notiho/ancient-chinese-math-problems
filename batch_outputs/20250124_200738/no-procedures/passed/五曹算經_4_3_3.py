"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 900 hu of millet, and for each hu, an additional 2 dou and 5 sheng are added.
Question: how much is the total addition?

Answer: *a* hu.
"""

from fractions import Fraction

# 粟九百斛
粟 = 900

# 每斛加 2斗5升 (convert to hu: 1 hu = 10 dou, 1 dou = 10 sheng)
加量每斛 = Fraction(2, 10) + Fraction(5, 100)

# 總加量
a = 粟 * 加量每斛

# Result
a#----- content ends here -----

"""
"""
