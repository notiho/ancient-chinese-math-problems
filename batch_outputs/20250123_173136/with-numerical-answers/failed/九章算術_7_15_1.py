"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a(=14)寸 ，重 b(=49/8)斤 。石 c(=13)寸 ，重 d(=39/8)斤 。
"""

"""
Suppose there is a cubic piece of jade with a side length of 1 cun, weighing 7 liang; and a cubic piece of stone with a side length of 1 cun, weighing 6 liang.
Now, there is a cubic block of stone with a side length of 3 cun, containing jade inside, and the total weight is 11 jin.
Question: how much jade and stone are there respectively, and what are their weights?

The procedure says: Suppose the entire block is jade, then it is 13 liang too heavy.
Suppose the entire block is stone, then it is 14 liang too light.
The excess is jade, and the deficit is stone.
Multiply each by the weight per cun^3, obtaining the total weight of jade and stone.

Answer: The jade is *a*(=14) cun^3, weighing *b*(=49/8) jin. The stone is *c*(=13) cun^3, weighing *d*(=39/8) jin.
"""

# 玉方一寸，重七兩
玉重每寸 = 7  # liang

# 石方一寸，重六兩
石重每寸 = 6  # liang

# 石立方三寸，中有玉，并重十一斤
總體積 = 3**3  # cun^3
總重量 = 11 * 16  # Convert jin to liang (1 jin = 16 liang)

# 假令皆玉，多十三兩
假皆玉重量 = 玉重每寸 * 總體積
多重量 = 假皆玉重量 - 総重量  # 13 liang

# 令之皆石，不足十四兩
假皆石重量 = 石重每寸 * 總體積
不足重量 = 總重量 - 假皆石重量  # 14 liang

# 不足為玉，多為石
玉體積 = Fraction(多重量, (多重量 + 不足重量)) * 總體積  # 玉的體積
石體積 = 總體積 - 玉體積  # 石的體積

# 各以一寸之重乘之，得玉石之積重
玉重量 = 玉體積 * 玉重每寸  # liang
石重量 = 石體積 * 石重每寸  # liang

# Convert weights to jin
b = Fraction(玉重量, 16)  # 玉重 in jin
d = Fraction(石重量, 16)  # 石重 in jin

# Final results
a = 玉體積  # 玉的體積
c = 石體積  # 石的體積
"""
Code error: name '総重量' is not defined"""
