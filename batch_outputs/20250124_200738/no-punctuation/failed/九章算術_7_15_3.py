"""
今有玉方一寸重七兩石方一寸重六兩今有石立方三寸中有玉并重十一斤問玉石重各幾何
術曰假令皆玉多十三兩令之皆石不足十四兩不足為玉多為石各以一寸之重乘之得玉石之積重
荅曰玉 a寸 重 b斤 石 c寸 重 d斤 
"""

#----- content starts here -----
"""
Suppose there is jade, where a cube of 1 cun weighs 7 liang, and stone, where a cube of 1 cun weighs 6 liang.
Now there is a cube of 3 cun, made of both jade and stone, with a total weight of 11 jin.
Question: how much jade and stone are there, and what are their respective weights?

The procedure says: Suppose it is all jade, and it exceeds by 13 liang.
Suppose it is all stone, and it falls short by 14 liang.
The excess is attributed to jade, and the shortfall is attributed to stone.
Multiply each by the weight of 1 cun to obtain the respective volumes and weights of jade and stone.

Answer: the jade is *a* cun, weighing *b* jin; the stone is *c* cun, weighing *d* jin.
"""

# 玉方一寸重七兩
玉重每寸 = 7  # liang

# 石方一寸重六兩
石重每寸 = 6  # liang

# 立方三寸
總體積 = 3  # cun^3

# 并重十一斤
總重量 = 11 * 16  # Convert jin to liang (1 jin = 16 liang)

# 假令皆玉，多十三兩
假皆玉重量 = 玉重每寸 * 總體積
多量 = 假皆玉重量 - 總重量  # 多十三兩

# 假令皆石，不足十四兩
假皆石重量 = 石重每寸 * 總體積
不足量 = 總重量 - 假皆石重量  # 不足十四兩

# 玉的體積
玉體積 = Fraction(不足量, 多量 + 不足量) * 總體積

# 石的體積
石體積 = 總體積 - 玉體積

# 玉的重量
玉重量 = 玉體積 * 玉重每寸

# 石的重量
石重量 = 石體積 * 石重每寸

# Convert weights back to jin
a = 玉體積
b = Fraction(玉重量, 16)  # Convert liang to jin
c = 石體積
d = Fraction(石重量, 16)  # Convert liang to jin#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14, Actual: 158
Variable 'b' has wrong value. Expected: 49/8, Actual: 553/8
Variable 'c' has wrong value. Expected: 13, Actual: -155
Variable 'd' has wrong value. Expected: 39/8, Actual: -465/8"""
