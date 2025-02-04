"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a(=14)寸 ，重 b(=49/8)斤 。石 c(=13)寸 ，重 d(=39/8)斤 。
"""

#----- content starts here -----
"""
Suppose there is a cubic piece of jade measuring 1 cun on each side, weighing 7 liang; and a cubic piece of stone measuring 1 cun on each side, weighing 6 liang.
Now, there is a cubic block of stone measuring 3 cun on each side, with some portion made of jade, and the total weight is 11 jin.
Question: how much jade and stone are there, and how much do they weigh respectively?

The procedure says: Suppose the entire block is jade, it would weigh 13 liang more than the actual weight.
Suppose the entire block is stone, it would weigh 14 liang less than the actual weight.
The shortage corresponds to jade, and the excess corresponds to stone.
Multiply each by the weight per cun of jade and stone, obtaining the total weight of jade and stone.

Answer: The jade measures *a*(=14) cun³, weighing *b*(=49/8) jin.
The stone measures *c*(=13) cun³, weighing *d*(=39/8) jin.
"""

# 玉方一寸，重七兩
玉重每寸 = 7  # liang

# 石方一寸，重六兩
石重每寸 = 6  # liang

# 石立方三寸，中有玉，并重十一斤
總體積 = 3**3  # 立方寸
總重量 = 11 * 16  # 斤 to liang (1 斤 = 16 liang)

# 假令皆玉，多十三兩
假玉重量 = 玉重每寸 * 總體積
多重量 = 假玉重量 - 總重量  # 13 liang

# 令之皆石，不足十四兩
假石重量 = 石重每寸 * 總體積
不足重量 = 總重量 - 假石重量  # 14 liang

# 不足為玉，多為石
玉體積 = 多重量  # 13 liang corresponds to 玉
石體積 = 不足重量  # 14 liang corresponds to 石

# 各以一寸之重乘之，得玉石之積重
玉重量 = 玉體積 * 玉重每寸  # liang
石重量 = 石體積 * 石重每寸  # liang

# Convert weights to jin
b = Fraction(玉重量, 16)  # 玉重 in jin
d = Fraction(石重量, 16)  # 石重 in jin

# Final results
a = 玉體積  # 玉體積 = 14 cun³
c = 石體積  # 石體積 = 13 cun³#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14, Actual: 13
Variable 'b' has wrong value. Expected: 49/8, Actual: 91/16
Variable 'c' has wrong value. Expected: 13, Actual: 14
Variable 'd' has wrong value. Expected: 39/8, Actual: 21/4"""
