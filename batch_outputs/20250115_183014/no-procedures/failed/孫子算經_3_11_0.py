"""
今有粟，三十六萬九千九百八十斛七斗，在倉九年，年斛耗三升。問：一年、九年各耗幾何？
答曰： a年 耗 b斛 ， c年 耗 d斛 。
"""

"""
Suppose there are 369,980 hu and 7 dou of millet stored in a granary for 9 years. Each year, 3 sheng per hu is lost due to wastage.
Question: how much is lost in one year, and how much is lost in nine years?

Answer: In *a* years, *b* hu are lost. In *c* years, *d* hu are lost.
"""

# 粟總量
粟總量 = 369980 + Fraction(7, 10)  # Convert 7 dou to fractional hu (1 dou = 1/10 hu)

# 每年每斛耗三升
每年耗升 = Fraction(3, 10)  # 3 sheng = 3/10 hu

# 一年耗
a = 1
b = 每年耗升 * 粟總量

# 九年耗
c = 9
d = 每年耗升 * 粟總量 * 9

# Results
a, b, c, d
"""
Variable 'b' has wrong value. Expected: 11099421/1000, Actual: 11099421/100
Variable 'd' has wrong value. Expected: 99894789/1000, Actual: 99894789/100"""
