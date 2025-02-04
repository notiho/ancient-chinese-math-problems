"""
今有粟，二千三百七十四斛，斛加三升。問：共粟幾何？
答曰： a斛 。
"""

"""
Suppose there is millet, 2374 hu, and each hu is increased by 3 sheng.
Question: how much millet is there in total?

Answer: *a* hu.
"""

from fractions import Fraction

# 粟二千三百七十四斛
粟 = 2374

# 每斛加三升
每斛增加 = Fraction(3, 10)  # 1 hu = 10 sheng, so 3 sheng = 3/10 hu

# 計算總粟
a = 粟 + 粟 * 每斛增加

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 122261/50, Actual: 15431/5"""
