"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a(=8000)尺 。為粟 b(=80000/27)斛 。
"""

"""
Suppose there is a pile of millet on flat ground, with a base circumference of 12 zhang and a height of 2 zhang.
Question: what is the volume, and how much millet does it contain?

The procedure for piled millet says: Multiply the base circumference by itself, then multiply by the height, and divide by 36.
If it leans against a wall, divide by 18.
If it leans against an inner corner, divide by 9.
For millet, 1 hu occupies 2 chi 7 cun of volume.
For rice, 1 hu occupies 1 chi 6 cun and 1/5 cun of volume.
For beans, da, hemp, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: the volume is *a*(=8000) chi³, and the millet is *b*(=80000/27) hu.
"""

# 下周一十二丈
下周 = 12 * 10  # Convert zhang to chi

# 高二丈
高 = 2 * 10  # Convert zhang to chi

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 三十六而一
積 = Fraction(積, 36)

# 積二尺七寸 (Convert 2 chi 7 cun to chi)
粟每斛積 = 2 + Fraction(7, 10)

# 為粟幾何
粟 = Fraction(積, 粟每斛積)

a = 積  # 8000 chi³
b = 粟  # 80000/27 hu
"""
"""
