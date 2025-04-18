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
粟斛 = 3999
粟斗 = 9
粟升 = 6

# 轉換為斗 (1斛 = 10斗, 1斗 = 10升)
總粟斗 = 粟斛 * 10 + 粟斗 + Fraction(粟升, 10)

# 九斗易豆一斛
法 = 9

# 實如法，即得
a = Fraction(總粟斗, 法)
#----- content ends here -----


"""
 

`a` represents the number of 豆斛 obtained.
"""


"""
"""
