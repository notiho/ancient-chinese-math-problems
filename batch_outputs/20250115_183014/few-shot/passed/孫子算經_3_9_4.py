"""
今有粟，三千九百九十九斛九斗六升，凡粟九斗易豆一斛。問：計豆幾何？
術曰：置粟三千九百九十九斛九斗六升為實，以九斗為法。實如法，即得。
答曰： a斛 。
"""

"""
Suppose there are 3999 hu, 9 dou, and 6 sheng of millet. 
For every 9 dou of millet, 1 hu of beans can be exchanged.
Question: how many hu of beans can be obtained?

The procedure says: Place 3999 hu, 9 dou, and 6 sheng of millet as the dividend.
Take 9 dou as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟三千九百九十九斛九斗六升
粟_斛 = 3999
粟_斗 = 9
粟_升 = 6

# 1斛 = 10斗, 1斗 = 10升
# Convert everything to 升 for uniformity
粟_總升 = (粟_斛 * 10 * 10) + (粟_斗 * 10) + 粟_升

# 每九斗易一斛
法 = 9 * 10  # 9斗 = 90升

# 實如法，即得
a = Fraction(粟_總升, 法)  # Convert total millet into beans in hu
"""
"""
