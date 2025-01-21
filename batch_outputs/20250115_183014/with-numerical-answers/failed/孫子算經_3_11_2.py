"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰： a(=1)年 耗 b(=11099421/1000)斛 ， c(=9)年 耗 d(=99894789/1000)斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years. 
Each year, 3 sheng per hu are lost due to wastage.
Question: how much is wasted in 1 year and in 9 years?

The procedure says: Place 369,980 hu and 7 dou. Multiply it by 3 sheng to obtain the wastage for 1 year.
Then multiply it by 9 to obtain the wastage for 9 years.

Answer: *a*(=1) year wastes *b*(=11099421/1000) hu, and *c*(=9) years waste *d*(=99894789/1000) hu.
"""

# 粟三十六萬九千九百八十斛七斗
粟_斛 = 369980
粟_斗 = 7

# Convert dou to hu (10 dou = 1 hu)
粟 = 粟_斛 + Fraction(粟_斗, 10)

# 年斛耗三升
年耗_升 = 3

# Convert sheng to hu (1000 sheng = 1 hu)
年耗 = Fraction(年耗_升, 1000)

# 一年耗
b = 粟 * 年耗

# 九年耗
c = 9
d = b * c

a = 1  # 1 year

"""
Variable 'b' has wrong value. Expected: 11099421/1000, Actual: 11099421/10000
Variable 'd' has wrong value. Expected: 99894789/1000, Actual: 99894789/10000"""
