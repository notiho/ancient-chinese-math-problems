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
Multiply it by 3 sheng to obtain the loss for one year.
Then multiply it by 9 to obtain the loss for nine years.

Answer: the loss for one year is *a*(=11099421/1000) hu, and the loss for nine years is *b*(=99894789/1000) hu.
"""

# 粟三十六萬九千九百八十斛七斗
粟 = Fraction(369980, 1) + Fraction(7, 10)  # Convert 7 dou to hu (1 dou = 1/10 hu)

# 年斛耗三升
年耗率 = Fraction(3, 10)  # Convert 3 sheng per hu to hu (1 sheng = 1/10 dou = 1/100 hu)

# 一年耗
a = 粟 * 年耗率  # 11099421/1000 hu

# 九年耗
b = a * 9  # 99894789/1000 hu
"""
Variable 'a' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'b' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
