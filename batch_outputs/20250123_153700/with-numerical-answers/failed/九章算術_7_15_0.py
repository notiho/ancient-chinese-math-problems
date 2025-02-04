"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a(=14)寸 ，重 b(=49/8)斤 。石 c(=13)寸 ，重 d(=39/8)斤 。
"""

"""
Suppose there is a cubic jade block of 1 cun, weighing 7 liang, and a cubic stone block of 1 cun, weighing 6 liang.
Now, there is a cubic stone block of 3 cun, with a jade block inside, and together they weigh 11 jin.
Question: how much do the jade and stone weigh respectively?

The procedure says: Suppose all is jade, it exceeds by 13 liang.
Suppose all is stone, it falls short by 14 liang.
The shortfall is jade, and the excess is stone.
Multiply each by the weight of 1 cun, obtaining the total weight of jade and stone.

Answer: The jade is *a*(=14) cun, weighing *b*(=49/8) jin.
The stone is *c*(=13) cun, weighing *d*(=39/8) jin.
"""

# 玉方一寸，重七兩
玉重每寸 = 7

# 石方一寸，重六兩
石重每寸 = 6

# 石立方三寸
總體積 = 3

# 并重十一斤
總重量 = 11 * 16  # 1 斤 = 16 兩

# 假令皆玉，多十三兩
假皆玉重量 = 玉重每寸 * 總體積
多量 = 假皆玉重量 - 總重量  # 13 兩

# 令之皆石，不足十四兩
假皆石重量 = 石重每寸 * 總體積
不足量 = 總重量 - 假皆石重量  # 14 兩

# 不足為玉，多為石
玉體積 = 不足量  # 玉體積 = 14 寸
石體積 = 多量  # 石體積 = 13 寸

# 各以一寸之重乘之，得玉石之積重
玉重量 = 玉體積 * 玉重每寸
石重量 = 石體積 * 石重每寸

# 轉換為斤
a = 玉體積  # 14 寸
b = Fraction(玉重量, 16)  # 49/8 斤
c = 石體積  # 13 寸
d = Fraction(石重量, 16)  # 39/8 斤
"""
Variable 'a' has wrong value. Expected: 14, Actual: 158
Variable 'b' has wrong value. Expected: 49/8, Actual: 553/8
Variable 'c' has wrong value. Expected: 13, Actual: -155
Variable 'd' has wrong value. Expected: 39/8, Actual: -465/8"""
