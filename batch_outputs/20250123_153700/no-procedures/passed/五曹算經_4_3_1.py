"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
答曰： a斛 。
"""

"""
Suppose there are 900 hu of millet. For each hu, an additional 2 dou and 5 sheng are added.
Question: how much is the total addition?

Answer: *a* hu.
"""

from fractions import Fraction

# 粟九百斛
粟 = 900

# 每斛加二斗五升 (convert to hu: 1 hu = 10 dou, 1 dou = 10 sheng)
加量 = Fraction(2 * 10 + 5, 100)  # Convert 2 dou 5 sheng to hu

# 總加量
a = 粟 * 加量

# Output the result
a
"""
"""
