"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a(=11099421/1000)斛 ，九年耗 b(=99894789/1000)斛 。
"""

#----- content starts here -----
"""
Suppose there is millet, 369,980 hu and 7 dou, stored in a granary for 9 years. Each year, 3 sheng per hu is lost.
Question: how much is lost in one year and in nine years?

The procedure says: Place 369,980 hu and 7 dou. Multiply it by 3 sheng to obtain the loss for one year. Then multiply it by 9 to obtain the loss for nine years.

Answer: the loss for one year is *a*(=11099421/1000) hu, and the loss for nine years is *b*(=99894789/1000) hu.
"""

# 粟三十六萬九千九百八十斛七斗
粟斛 = 369980
粟斗 = 7

# Convert 7斗 to hu (1斗 = 1/10 hu)
粟 = 粟斛 + Fraction(粟斗, 10)

# 年斛耗三升
年耗升 = 3

# Convert 3升 to hu (1升 = 1/100 hu)
年耗 = Fraction(年耗升, 100)

# 一年耗
一年耗 = 粟 * 年耗

# 九年耗
九年耗 = 一年耗 * 9

# Results
a = 一年耗  # 11099421/1000 hu
b = 九年耗  # 99894789/1000 hu#----- content ends here -----

"""
"""
