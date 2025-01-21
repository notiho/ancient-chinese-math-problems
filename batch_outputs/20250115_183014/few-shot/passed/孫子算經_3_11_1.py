"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰： a年 耗 b斛 ， c年 耗 d斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years. Each year, 3 sheng per hu are lost.
Question: how much is lost in one year and in nine years?

The procedure says: Place 369,980 hu and 7 dou, and multiply it by 3 sheng, obtaining the loss for one year. Then multiply it by 9, obtaining the loss for nine years.

Answer: *a* year loses *b* hu, *c* years lose *d* hu.
"""

from fractions import Fraction

# 粟三十六萬九千九百八十斛七斗
粟_斛 = 369980
粟_斗 = 7

# Convert 7斗 to 斛 (10斗 = 1斛)
粟 = 粟_斛 + Fraction(粟_斗, 10)

# 年斛耗三升
年耗升 = 3

# Convert 3升 to 斛 (1斛 = 100升)
年耗斛 = Fraction(年耗升, 100)

# 一年耗
一年耗 = 粟 * 年耗斛

# 九年耗
九年耗 = 一年耗 * 9

# Results
a = 1
b = 一年耗
c = 9
d = 九年耗
"""
"""
