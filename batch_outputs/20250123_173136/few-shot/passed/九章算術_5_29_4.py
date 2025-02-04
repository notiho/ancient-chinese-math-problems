"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為粟 b斛 。
"""

"""
Suppose there is a pile of millet on flat ground. The base circumference is 12 zhang, and the height is 2 zhang.
Question: what is the volume, and how much millet does it make?

The procedure for piled millet says: Multiply the base circumference by itself, then multiply by the height, and divide by 36 to get the volume.
If it is against a wall, divide by 18. If it is in an inner corner, divide by 9.
For millet, 1 hu occupies 2 chi 7 cun of volume.
For rice, 1 hu occupies 1 chi 6 cun and 1/5 cun of volume.
For beans, da, hemp, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: the volume is *a* chi³, and it makes *b* hu of millet.
"""

# 下周一十二丈
下周 = 12  # 丈

# 高二丈
高 = 2  # 丈

# 下周自乘
下周積 = 下周 * 下周

# 以高乘之
體積 = 下周積 * 高

# 三十六而一
體積 = Fraction(體積, 36)

# 積 a尺
a = 體積 * 1000  # Convert from 丈³ to 尺³ (1 丈³ = 1000 尺³)

# 程粟一斛，積二尺七寸
粟每斛體積 = 2 + Fraction(7, 10)  # 2 尺 7 寸 = 2.7 尺³

# 為粟 b斛
b = Fraction(a, 粟每斛體積)
"""
"""
