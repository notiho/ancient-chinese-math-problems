"""
今有粟，三千九百九十九斛九斗六升，凡粟九斗易豆一斛。問：計豆幾何？
術曰：置粟三千九百九十九斛九斗六升為實，以九斗為法。實如法，即得。
答曰： a斛 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 粟三千九百九十九斛九斗六升
粟_斛 = 3999
粟_斗 = 9
粟_升 = 6

# 1斛 = 10斗, 1斗 = 10升
總粟升 = 粟_斛 * 10 * 10 + 粟_斗 * 10 + 粟_升

# 九斗易豆一斛
法 = 9 * 10  # 9斗 = 90升

# 實如法，即得
a = Fraction(總粟升, 法)
#----- content ends here -----


"""

"""


"""
"""
