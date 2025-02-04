"""
今有粟三千九百九十九斛九斗六升凡粟九斗易豆一斛問計豆幾何
術曰置粟三千九百九十九斛九斗六升為實以九斗為法實如法即得
答曰 a斛 
"""

"""
Suppose there are 3999 hu, 9 dou, and 6 sheng of millet. 
For every 9 dou of millet, it is exchanged for 1 hu of beans.
Question: how many hu of beans are obtained?

The procedure says: Place 3999 hu, 9 dou, and 6 sheng of millet as the dividend.
Take 9 dou as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: *a* hu of beans.
"""

from fractions import Fraction

# 粟三千九百九十九斛九斗六升
粟_斛 = 3999
粟_斗 = 9
粟_升 = 6

# Convert everything to dou (1 hu = 10 dou, 1 dou = 10 sheng)
粟_總斗 = (粟_斛 * 10) + 粟_斗 + Fraction(粟_升, 10)

# 以九斗為法
法 = 9

# 實如法即得
a = Fraction(粟_總斗, 法)  # Result in hu of beans
"""
"""
