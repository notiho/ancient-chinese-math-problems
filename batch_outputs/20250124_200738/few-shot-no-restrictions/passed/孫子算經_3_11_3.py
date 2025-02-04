"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

#----- content starts here -----
"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years.
Each year, 3 sheng per hu is lost due to wastage.
Question: how much is wasted in one year, and how much in nine years?

The procedure says: Place 369,980 hu and 7 dou, and multiply it by 3 sheng to obtain the wastage for one year.
Then multiply it by 9 to obtain the wastage for nine years.

Answer: *a* hu is wasted in one year, and *b* hu is wasted in nine years.
"""

from fractions import Fraction

# 粟數：三十六萬九千九百八十斛七斗
粟_斛 = 369980
粟_斗 = 7

# Convert 粟 to total hu (1 斗 = 1/10 斛)
粟 = 粟_斛 + Fraction(粟_斗, 10)

# 年斛耗三升
年耗升 = 3

# Convert 年耗升 to hu (1 hu = 10 dou = 100 sheng)
年耗_每斛 = Fraction(年耗升, 100)

# 一年耗
一年耗 = 粟 * 年耗_每斛

# 九年耗
九年耗 = 一年耗 * 9

# Results
a = 一年耗
b = 九年耗

# Output
a, b#----- content ends here -----

"""
"""
