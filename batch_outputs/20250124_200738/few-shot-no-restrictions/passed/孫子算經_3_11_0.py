"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

#----- content starts here -----
"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years.
Each year, 3 sheng per hu is lost due to spoilage.
Question: how much is lost in 1 year and in 9 years?

The procedure says: Take 369,980 hu and 7 dou, multiply it by 3 sheng to get the loss for 1 year.
Then multiply it by 9 to get the loss for 9 years.

Answer: the loss for 1 year is *a* hu, and the loss for 9 years is *b* hu.
"""

from fractions import Fraction

# 粟三十六萬九千九百八十斛七斗
粟_斛 = 369980  # Total hu
粟_斗 = 7  # Additional dou

# Convert dou to hu (1 hu = 10 dou)
粟 = 粟_斛 + Fraction(粟_斗, 10)

# 年斛耗三升
年耗升 = 3  # Loss per hu per year in sheng

# Convert sheng to hu (1 hu = 100 sheng)
年耗 = Fraction(年耗升, 100)  # Loss per hu per year in hu

# 一年耗
一年耗 = 粟 * 年耗

# 九年耗
九年耗 = 一年耗 * 9

# Results
a = 一年耗
b = 九年耗

# Output
a, b#----- content ends here -----

"""
"""
