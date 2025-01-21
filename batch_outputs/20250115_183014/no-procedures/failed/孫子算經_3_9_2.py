"""
今有粟，三千九百九十九斛九斗六升，凡粟九斗易豆一斛。問：計豆幾何？
答曰： a斛 。
"""

"""
Suppose there is millet, totaling 3999 hu, 9 dou, and 6 sheng. 
For every 9 dou of millet, 1 hu of beans can be exchanged.
Question: how many hu of beans can be obtained?

Answer: *a* hu.
"""

from fractions import Fraction

# 粟的總量：3999斛9斗6升
粟_斛 = 3999
粟_斗 = 9
粟_升 = 6

# Convert everything to dou (1斛 = 10斗, 1斗 = 10升)
粟_總斗 = 粟_斛 * 10 + 粟_斗 + Fraction(粟_升, 10)

# 每9斗粟可換1斛豆
豆_斛 = 粟_總斗 // 9

# 答案
a = 豆_斛
a
"""
Variable 'a' has wrong value. Expected: 22222/5, Actual: 4444"""
