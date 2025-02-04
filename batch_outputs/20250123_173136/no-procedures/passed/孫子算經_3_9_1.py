"""
今有粟，三千九百九十九斛九斗六升，凡粟九斗易豆一斛。問：計豆幾何？
答曰： a斛 。
"""

"""
Suppose there is millet, totaling 3999 hu, 9 dou, and 6 sheng. 
For every 9 dou of millet, it can be exchanged for 1 hu of beans.
Question: how many hu of beans can be obtained?

Answer: *a* hu.
"""

from fractions import Fraction

# Total millet in hu, dou, and sheng
粟_斛 = 3999
粟_斗 = 9
粟_升 = 6

# Convert everything to dou (1 hu = 10 dou, 1 dou = 10 sheng)
total_dou = 粟_斛 * 10 + 粟_斗 + Fraction(粟_升, 10)

# For every 9 dou of millet, 1 hu of beans is obtained
a = Fraction(total_dou, 9)

# Result
a
"""
"""
