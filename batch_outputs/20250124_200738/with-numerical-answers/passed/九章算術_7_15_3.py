"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a(=14)寸 ，重 b(=49/8)斤 。石 c(=13)寸 ，重 d(=39/8)斤 。
"""

#----- content starts here -----
"""
Suppose there is a cubic piece of jade with a side length of 1 cun, weighing 7 liang; and a cubic piece of stone with a side length of 1 cun, weighing 6 liang.
Now, there is a cube with a side length of 3 cun, containing jade and stone, and the total weight is 11 jin.
Question: how much jade and stone are there, and how much do they weigh respectively?

The procedure says: Suppose it is all jade, the weight exceeds by 13 liang. Suppose it is all stone, the weight falls short by 14 liang.
The excess corresponds to jade, and the shortfall corresponds to stone.
Multiply each by the weight of 1 cun^3, obtaining the total weight of jade and stone.

Answer: The jade is *a*(=14) cun^3, weighing *b*(=49/8) jin. The stone is *c*(=13) cun^3, weighing *d*(=39/8) jin.
"""

# 玉方一寸，重七兩；石方一寸，重六兩
玉重每寸 = 7  # liang
石重每寸 = 6  # liang

# 立方三寸
立方邊長 = 3  # cun
立方體積 = 立方邊長 ** 3  # cun^3

# 并重十一斤
總重 = 11 * 16  # 11 jin converted to liang (1 jin = 16 liang)

# 假令皆玉，多十三兩
假皆玉重 = 玉重每寸 * 立方體積
多量 = 假皆玉重 - 總重  # 13 liang

# 令之皆石，不足十四兩
假皆石重 = 石重每寸 * 立方體積
不足量 = 總重 - 假皆石重  # 14 liang

# 不足為玉，多為石
玉體積 = 不足量  # 14 cun^3
石體積 = 多量  # 13 cun^3

# 各以一寸之重乘之，得玉石之積重
玉重量 = 玉體積 * 玉重每寸  # in liang
石重量 = 石體積 * 石重每寸  # in liang

# Convert weights back to jin
b = Fraction(玉重量, 16)  # 玉重 in jin
d = Fraction(石重量, 16)  # 石重 in jin

# Final results
a = 玉體積  # 14 cun^3
c = 石體積  # 13 cun^3#----- content ends here -----

"""
"""
