"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a(=14)寸 ，重 b(=49/8)斤 。石 c(=13)寸 ，重 d(=39/8)斤 。
"""

"""
Suppose there is a cubic jade block of 1 cun, weighing 7 liang, and a cubic stone block of 1 cun, weighing 6 liang.
Now, there is a cubic stone block of 3 cun, with some jade inside, and the total weight is 11 jin.
Question: how much do the jade and stone weigh respectively?

The procedure says: Suppose it is all jade, it exceeds by 13 liang.
Suppose it is all stone, it falls short by 14 liang.
The shortfall corresponds to the jade, and the excess corresponds to the stone.
Multiply each by the weight per cun to find the total weight of the jade and stone.

Answer: The jade is *a*(=14) cun, weighing *b*(=49/8) jin.
The stone is *c*(=13) cun, weighing *d*(=39/8) jin.
"""

# 玉方一寸，重七兩
玉重每寸 = 7  # in liang

# 石方一寸，重六兩
石重每寸 = 6  # in liang

# 石立方三寸，中有玉，并重十一斤
總體積 = 3  # in cubic cun
總重量 = 11 * 16  # convert jin to liang (1 jin = 16 liang)

# 假令皆玉，多十三兩
假皆玉重量 = 玉重每寸 * 總體積
多量 = 假皆玉重量 - 總重量  # 13 liang

# 令之皆石，不足十四兩
假皆石重量 = 石重每寸 * 總體積
不足量 = 總重量 - 假皆石重量  # 14 liang

# 不足為玉，多為石
玉體積 = 多量  # 13 cun
石體積 = 不足量  # 14 cun

# 各以一寸之重乘之，得玉石之積重
玉重量 = 玉體積 * 玉重每寸  # in liang
石重量 = 石體積 * 石重每寸  # in liang

# Convert weights back to jin
b = Fraction(玉重量, 16)  # 玉重 in jin
d = Fraction(石重量, 16)  # 石重 in jin

# Final results
a = 玉體積  # 14 cun
c = 石體積  # 13 cun
"""
Variable 'a' has wrong value. Expected: 14, Actual: -155
Variable 'b' has wrong value. Expected: 49/8, Actual: -1085/16
Variable 'c' has wrong value. Expected: 13, Actual: 158
Variable 'd' has wrong value. Expected: 39/8, Actual: 237/4"""
