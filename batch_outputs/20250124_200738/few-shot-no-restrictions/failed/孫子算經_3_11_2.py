"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
術曰：置三十六萬九千九百八十斛七斗，以三升乘之，得一年之耗，又以九乘之，即九年之耗。
答曰：一年耗 a斛 ，九年耗 b斛 。
"""

#----- content starts here -----
"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years.
Each year, 3 sheng per hu are consumed.
Question: how much is consumed in one year, and how much in nine years?

The procedure says: Place 369,980 hu and 7 dou, and multiply by 3 sheng to obtain the yearly consumption.
Then multiply by 9 to obtain the consumption over 9 years.

Answer: the yearly consumption is *a* hu, and the 9-year consumption is *b* hu.
"""

from fractions import Fraction

# 粟三十六萬九千九百八十斛七斗
粟_斛 = 369980
粟_斗 = 7

# Convert 7 斗 to 斛 (1 斛 = 10 斗)
粟 = 粟_斛 + Fraction(粟_斗, 10)

# 年斛耗三升 (3 升 per 1 斛)
年耗率 = Fraction(3, 10)  # 3 升 = 0.3 斛

# 一年之耗
一年耗 = 粟 * 年耗率

# 九年之耗
九年耗 = 一年耗 * 9

# Results
a = 一年耗
b = 九年耗

# Output
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
