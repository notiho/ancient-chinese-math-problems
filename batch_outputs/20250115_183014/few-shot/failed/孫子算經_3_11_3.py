"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰： a年 耗 b斛 ， c年 耗 d斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years. Each year, 3 sheng per hu is lost.
Question: how much is lost in 1 year and in 9 years?

The procedure says: Place 369,980 hu and 7 dou. Multiply it by 3 sheng to obtain the loss for 1 year. Then multiply it by 9 to obtain the loss for 9 years.

Answer: *a* year loses *b* hu, *c* years lose *d* hu.
"""

from fractions import Fraction

# 粟三十六萬九千九百八十斛七斗
粟_斛 = 369980
粟_斗 = 7

# Convert 7斗 to 斛 (1斛 = 10斗)
粟 = 粟_斛 + Fraction(粟_斗, 10)

# 年斛耗三升
年耗_升 = 3

# 1斛 = 10斗 = 100升, convert 3升 to fraction of 1斛
年耗率 = Fraction(年耗_升, 100)

# 一年之耗
一年耗 = 粟 * 年耗率

# 九年之耗
九年耗 = 一年耗 * 9

# Convert results back to hu and dou
b = int(一年耗)  # Whole hu for 1 year
b_斗 = (一年耗 - b) * 10  # Remaining dou for 1 year

d = int(九年耗)  # Whole hu for 9 years
d_斗 = (九年耗 - d) * 10  # Remaining dou for 9 years

# Answer
a = 1
c = 9

# Results
b = f"{b}斛 {b_斗}斗"
d = f"{d}斛 {d_斗}斗"
"""
Variable 'b' has wrong value. Expected: 11099421/1000, Actual: 11099斛 421/100斗
Variable 'd' has wrong value. Expected: 99894789/1000, Actual: 99894斛 789/100斗"""
