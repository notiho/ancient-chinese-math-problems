"""
今有粟，三千九百九十九斛九斗六升，凡粟九斗易豆一斛。問：計豆幾何？
術曰：置粟三千九百九十九斛九斗六升為實，以九斗為法。實如法，即得。
答曰： a(=22222/5)斛 。
"""

"""
Suppose there is millet, 3999 hu, 9 dou, and 6 sheng in total. 
For every 9 dou of millet, exchange it for 1 hu of beans.
Question: how many hu of beans can be obtained?

The procedure says: Place the millet, 3999 hu, 9 dou, and 6 sheng, as the dividend.
Take 9 dou as the divisor.
Perform the division, and the result is obtained.

Answer: *a*(=22222/5) hu of beans.
"""

from fractions import Fraction

# 粟三千九百九十九斛九斗六升
粟_斛 = 3999
粟_斗 = 9
粟_升 = 6

# Convert all to dou (1 斛 = 10 斗, 1 斗 = 10 升)
粟_總斗 = (粟_斛 * 10) + 粟_斗 + Fraction(粟_升, 10)

# 以九斗為法
法 = 9

# 實如法，即得
a = Fraction(粟_總斗, 法) # 22222/5

"""
"""
