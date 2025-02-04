"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

#----- content starts here -----
"""
Suppose there is a jade cube of 1 cun, weighing 7 liang, and a stone cube of 1 cun, weighing 6 liang.
Now there is a stone cube of 3 cun on each side, with a jade cube inside it, and together they weigh 11 jin.
Question: how much do the jade and stone weigh respectively?

The procedure says: Suppose all is jade, then it exceeds by 13 liang.
Suppose all is stone, then it falls short by 14 liang.
The shortfall corresponds to jade, and the excess corresponds to stone.
Multiply each by the weight per cun to obtain the total weight of jade and stone.

Answer: the jade is *a* cun, weighing *b* jin. The stone is *c* cun, weighing *d* jin.
"""

# 玉方一寸，重七兩
玉重每寸 = 7  # liang

# 石方一寸，重六兩
石重每寸 = 6  # liang

# 石立方三寸
石立方 = 3 ** 3  # Total volume of the stone cube in cubic cun

# 并重十一斤
總重 = 11 * 16  # Convert total weight to liang (1 jin = 16 liang)

# 假令皆玉，多十三兩
假皆玉重 = 玉重每寸 * 石立方
多 = 假皆玉重 - 總重  # Excess weight in liang

# 令之皆石，不足十四兩
假皆石重 = 石重每寸 * 石立方
不足 = 總重 - 假皆石重  # Shortfall in liang

# 不足為玉，多為石
玉體積 = 不足  # The shortfall corresponds to the volume of jade in cubic cun
石體積 = 多  # The excess corresponds to the volume of stone in cubic cun

# 各以一寸之重乘之，得玉石之積重
玉重量 = 玉體積 * 玉重每寸
石重量 = 石體積 * 石重每寸

# Convert weights back to jin for the answer
b = 玉重量 // 16  # 玉重 in jin
d = 石重量 // 16  # 石重 in jin
a = 玉體積
c = 石體積#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 49/8, Actual: 6
Variable 'd' has wrong value. Expected: 39/8, Actual: 4"""
