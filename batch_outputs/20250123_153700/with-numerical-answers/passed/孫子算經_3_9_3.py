"""
今有粟，三千九百九十九斛九斗六升，凡粟九斗易豆一斛。問：計豆幾何？
術曰：置粟三千九百九十九斛九斗六升為實，以九斗為法。實如法，即得。
答曰： a(=22222/5)斛 。
"""

"""
Suppose there is millet, totaling 3999 hu, 9 dou, and 6 sheng.
For every 9 dou of millet, it is exchanged for 1 hu of beans.
Question: how many hu of beans can be obtained?

The procedure says: Place the millet, 3999 hu, 9 dou, and 6 sheng, as the dividend.
Take 9 dou as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a*(=22222/5) hu of beans.
"""

from fractions import Fraction

# 粟三千九百九十九斛九斗六升
粟_斛 = 3999
粟_斗 = 9
粟_升 = 6

# Convert everything to dou (1 hu = 10 dou, 1 dou = 10 sheng)
粟_總斗 = (粟_斛 * 10) + 粟_斗 + Fraction(粟_升, 10)

# 每九斗易豆一斛
法 = 9

# 實如法，即得
a = Fraction(粟_總斗, 法) # 22222/5

"""
"""
