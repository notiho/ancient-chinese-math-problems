"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a(=11099421/1000)斛 ，九年耗 b(=99894789/1000)斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years.
Each year, 3 sheng per hu are lost due to spoilage.
Question: how much is lost in one year and in nine years?

The procedure says: Place 369,980 hu and 7 dou.
Multiply it by 3 sheng, obtaining the loss for one year.
Then multiply it by 9, obtaining the loss for nine years.

Answer: the loss for one year is *a*(=11099421/1000) hu, and the loss for nine years is *b*(=99894789/1000) hu.
"""

# 粟三十六萬九千九百八十斛七斗
粟_斛 = 369980
粟_斗 = 7

# Convert 斗 to 斛 (1 斛 = 10 斗)
粟 = 粟_斛 + Fraction(粟_斗, 10)

# 年斛耗三升
年耗_升 = 3

# Convert 升 to 斛 (1 斛 = 100 升)
年耗_斛 = Fraction(年耗_升, 100)

# 一年之耗
一年耗 = 粟 * 年耗_斛

# 九年之耗
九年耗 = 一年耗 * 9

a = 一年耗  # 11099421/1000
b = 九年耗  # 99894789/1000
"""
"""
