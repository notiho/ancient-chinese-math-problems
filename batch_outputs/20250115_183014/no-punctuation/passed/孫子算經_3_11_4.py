"""
今有粟三十六萬九千九百八十斛七斗在倉九年年斛耗三升問一年九年各耗幾何
術曰置三十六萬九千九百八十斛七斗以三升乘之得一年之耗又以九乘之即九年之耗
答曰 a年 耗 b斛  c年 耗 d斛 
"""

"""
Suppose there are 369,980 hu and 7 dou of millet in a granary for 9 years.
Each year, 3 sheng per hu are lost due to spoilage.
Question: how much is lost in one year and in nine years?

The procedure says: Place 369,980 hu and 7 dou. Multiply it by 3 sheng to obtain the loss for one year.
Then multiply it by 9 to obtain the loss for nine years.

Answer: *a* year loses *b* hu, *c* years lose *d* hu.
"""

from fractions import Fraction

# 粟三十六萬九千九百八十斛七斗
粟_斛 = 369980
粟_斗 = 7

# Convert 斗 to 斛 (10斗 = 1斛)
粟 = 粟_斛 + Fraction(粟_斗, 10)

# 年斛耗三升
年耗升 = 3

# Convert 升 to 斛 (1斛 = 100升)
年耗斛 = Fraction(年耗升, 100)

# 置三十六萬九千九百八十斛七斗以三升乘之，得一年之耗
一年耗 = 粟 * 年耗斛

# 又以九乘之，即九年之耗
九年耗 = 一年耗 * 9

a = 1
b = 一年耗
c = 9
d = 九年耗
"""
"""
