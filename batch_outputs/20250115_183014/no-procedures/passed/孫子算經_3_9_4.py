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

# 粟的總量：3999斛9斗6升
粟_斛 = 3999
粟_斗 = 9
粟_升 = 6

# 1斛 = 10斗, 1斗 = 10升
# Convert everything to 升 for easier calculation
粟_總升 = 粟_斛 * 10 * 10 + 粟_斗 * 10 + 粟_升

# 每9斗（=90升）易1斛豆
換算率 = 9 * 10  # 90升 = 1斛豆

# 計算可換得的豆（斛）
a = Fraction(粟_總升, 換算率)

# Output the result
a
"""
"""
