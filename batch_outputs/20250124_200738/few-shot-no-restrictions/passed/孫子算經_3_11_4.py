"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

#----- content starts here -----
"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years.
Each year, 3 sheng per hu is lost due to wastage.
Question: how much is wasted in one year and in nine years?

The procedure says: Place 369,980 hu and 7 dou, and multiply it by 3 sheng to obtain the wastage for one year.
Then multiply it by 9 to obtain the wastage for nine years.

Answer: the wastage for one year is *a* hu, and the wastage for nine years is *b* hu.
"""

from fractions import Fraction

# 粟數：三十六萬九千九百八十斛七斗
粟_斛 = 369980
粟_斗 = 7

# Convert dou to hu (1 hu = 10 dou)
粟 = 粟_斛 + Fraction(粟_斗, 10)

# 年斛耗三升
年耗_升 = 3

# Convert sheng to hu (1 hu = 100升)
年耗_斛 = Fraction(年耗_升, 100)

# 一年耗
一年耗 = 粟 * 年耗_斛

# 九年耗
九年耗 = 一年耗 * 9

# Results
a = 一年耗
b = 九年耗

# Output the results
a, b#----- content ends here -----

"""
"""
