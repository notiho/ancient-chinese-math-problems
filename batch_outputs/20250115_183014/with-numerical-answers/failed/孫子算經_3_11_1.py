"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰： a(=1)年 耗 b(=11099421/1000)斛 ， c(=9)年 耗 d(=99894789/1000)斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years. Each year, 3 sheng per hu is consumed.
Question: how much is consumed in one year and in nine years?

The procedure says: Place 369,980 hu and 7 dou. Multiply it by 3 sheng to obtain the consumption for one year.
Then multiply it by 9 to obtain the consumption for nine years.

Answer: *a*(=1) year consumes *b*(=11099421/1000) hu, and *c*(=9) years consume *d*(=99894789/1000) hu.
"""

# 粟三十六萬九千九百八十斛七斗
粟斛 = 369980
粟斗 = 7

# Convert 7斗 to 斛 (1斛 = 10斗)
粟 = 粟斛 + Fraction(粟斗, 10)

# 年斛耗三升
年耗升 = 3

# 置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗
一年耗 = 粟 * Fraction(年耗升, 10)  # Convert 3升 to 0.3斛

# 又以九乘之，即九年之耗
九年耗 = 一年耗 * 9

# Results
a = 1
b = 一年耗  # 11099421/1000 hu
c = 9
d = 九年耗  # 99894789/1000 hu
"""
Variable 'b' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'd' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
