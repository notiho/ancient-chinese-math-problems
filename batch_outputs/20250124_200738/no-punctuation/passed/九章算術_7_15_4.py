"""
今有玉方一寸重七兩石方一寸重六兩今有石立方三寸中有玉并重十一斤問玉石重各幾何
術曰假令皆玉多十三兩令之皆石不足十四兩不足為玉多為石各以一寸之重乘之得玉石之積重
荅曰玉 a寸 重 b斤 石 c寸 重 d斤 
"""

#----- content starts here -----
"""
Suppose there is jade, where a cubic cun weighs 7 liang, and stone, where a cubic cun weighs 6 liang.
Now, there is a cube with a side length of 3 cun, containing both jade and stone, with a total weight of 11 jin.
Question: how much jade and stone are there, and what are their respective weights?

The procedure says: Suppose it is all jade, and it exceeds by 13 liang.
Suppose it is all stone, and it falls short by 14 liang.
The excess is jade, and the shortfall is stone.
For each, multiply by the weight of one cubic cun, obtaining the respective weights of jade and stone.

Answer: the jade is *a* cubic cun, weighing *b* jin, and the stone is *c* cubic cun, weighing *d* jin.
"""

# 玉方一寸重七兩
玉每寸重 = 7  # liang

# 石方一寸重六兩
石每寸重 = 6  # liang

# 石立方三寸中有玉并重十一斤
立方邊長 = 3  # cun
總重 = 11 * 16  # Convert jin to liang (1 jin = 16 liang)
總體積 = 立方邊長 ** 3  # Total volume in cubic cun

# 假令皆玉，多十三兩
假皆玉重 = 玉每寸重 * 總體積
多 = 假皆玉重 - 總重  # Excess weight in liang

# 令之皆石，不足十四兩
假皆石重 = 石每寸重 * 總體積
不足 = 總重 - 假皆石重  # Shortfall in liang

# 玉的體積
玉體積 = Fraction(不足, 多 + 不足) * 總體積

# 石的體積
石體積 = 總體積 - 玉體積

# 玉的重量
玉重量 = 玉體積 * 玉每寸重

# 石的重量
石重量 = 石體積 * 石每寸重

# Convert weights back to jin
a = 玉體積
b = Fraction(玉重量, 16)  # Convert liang to jin
c = 石體積
d = Fraction(石重量, 16)  # Convert liang to jin#----- content ends here -----

"""
"""
