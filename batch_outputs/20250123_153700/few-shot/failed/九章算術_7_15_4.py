"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

"""
Suppose there is a cubic jade block of 1 cun, weighing 7 liang, and a cubic stone block of 1 cun, weighing 6 liang.
Now there is a cubic stone block of 3 cun, with some jade inside, and the total weight is 11 jin.
Question: how much do the jade and stone weigh respectively?

The procedure says: Suppose it is all jade, then it exceeds by 13 liang.
Suppose it is all stone, then it is short by 14 liang.
The shortfall is jade, and the excess is stone.
Multiply each by the weight per cun to obtain the total weight of jade and stone.

Answer: The jade is *a* cun, weighing *b* jin. The stone is *c* cun, weighing *d* jin.
"""

# 玉方一寸，重七兩
玉重每寸 = 7  # liang

# 石方一寸，重六兩
石重每寸 = 6  # liang

# 石立方三寸，中有玉，并重十一斤
總體積 = 3  # cun^3
總重量 = 11 * 16  # Convert jin to liang (1 jin = 16 liang)

# 假令皆玉，多十三兩
假皆玉重量 = 玉重每寸 * 總體積
多量 = 假皆玉重量 - 総重量

# 令之皆石，不足十四兩
假皆石重量 = 石重每寸 * 總體積
不足量 = 總重量 - 假皆石重量

# 不足為玉，多為石
玉體積 = 不足量 / (多量 + 不足量) * 總體積
石體積 = 總體積 - 玉體積

# 各以一寸之重乘之，得玉石之積重
玉重量 = 玉體積 * 玉重每寸
石重量 = 石體積 * 石重每寸

# Convert weights back to jin
a = 玉體積
b = Fraction(玉重量, 16)  # Convert liang to jin
c = 石體積
d = Fraction(石重量, 16)  # Convert liang to jin
"""
Code error: name '総重量' is not defined"""
