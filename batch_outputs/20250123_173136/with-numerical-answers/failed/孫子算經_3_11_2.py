"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a(=11099421/1000)斛 ，九年耗 b(=99894789/1000)斛 。
"""

"""
Suppose there is millet, 369,980 hu and 7 dou, stored in a granary for 9 years.
Each year, 3 sheng per hu is consumed.
Question: how much is consumed in one year and in nine years?

The procedure says: Place 369,980 hu and 7 dou.
Multiply it by 3 sheng, obtaining the consumption for one year.
Then multiply it by 9, obtaining the consumption for nine years.

Answer: the consumption for one year is *a*(=11099421/1000) hu, and the consumption for nine years is *b*(=99894789/1000) hu.
"""

from fractions import Fraction

# 粟三十六萬九千九百八十斛七斗
粟斛 = 369980
粟斗 = 7

# Convert 7斗 to 斛 (1斛 = 10斗)
粟 = 粟斛 + Fraction(粟斗, 10)

# 年斛耗三升 (3升 per 1斛)
年耗率 = Fraction(3, 10)  # 3升 = 3/10斛

# 一年耗
一年耗 = 粟 * 年耗率

# 九年耗
九年耗 = 一年耗 * 9

# Results
a = 一年耗  # 11099421/1000
b = 九年耗  # 99894789/1000
"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
