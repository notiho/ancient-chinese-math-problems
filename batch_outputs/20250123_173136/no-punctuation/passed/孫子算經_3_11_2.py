"""
今有粟三十六萬九千九百八十斛七斗在倉九年年斛耗三升問一年九年各耗幾何
術曰置三十六萬九千九百八十斛七斗以三升乘之得一年之耗又以九乘之即九年之耗
答曰一年耗 a斛 九年耗 b斛 
"""

"""
Suppose there are 369,980 hu and 7 dou of millet in a granary for 9 years.
Each year, 3 sheng per hu are lost.
Question: how much is lost in one year and in nine years?

The procedure says: Place 369,980 hu and 7 dou.
Multiply it by 3 sheng to obtain the loss for one year.
Then multiply it by 9 to obtain the loss for nine years.

Answer: the loss for one year is *a* hu, and the loss for nine years is *b* hu.
"""

from fractions import Fraction

# 粟三十六萬九千九百八十斛七斗
粟_斛 = 369980
粟_斗 = 7

# Convert dou to hu (10 dou = 1 hu)
粟 = 粟_斛 + Fraction(粟_斗, 10)

# 年斛耗三升
年耗_升 = 3

# Convert sheng to hu (100 sheng = 1 hu)
年耗 = 粟 * Fraction(年耗_升, 100)

# 一年之耗
a = 年耗

# 九年之耗
b = 9 * 年耗
"""
"""
