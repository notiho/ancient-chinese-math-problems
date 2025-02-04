"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 粟三十六萬九千九百八十斛七斗
粟斛 = 369980
粟斗 = 7

# 轉換為斛（1斛 = 10斗）
粟 = 粟斛 + Fraction(粟斗, 10)

# 年斛耗三升
年耗升 = 3

# 置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗
一年耗 = 粟 * Fraction(年耗升, 10)

# 又以九乘之，即九年之耗
九年耗 = 一年耗 * 9

a = 一年耗
b = 九年耗
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
