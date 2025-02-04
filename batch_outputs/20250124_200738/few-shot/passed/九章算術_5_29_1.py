"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為粟 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground, with a base circumference of 12 zhang and a height of 2 zhang.
Question: what is the volume of the pile, and how much millet does it contain?

The procedure for piled millet says: Multiply the base circumference by itself, then multiply by the height, and divide by 36 to get the volume.
If the pile is against a wall, divide by 18.
If the pile is in a corner, divide by 9.
For millet, 1 hu occupies 2 chi 7 cun of volume.
For rice, 1 hu occupies 1 chi 6 cun and 1/5 cun of volume.
For beans, da, hemp, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: the volume is *a* chi, and the millet is *b* hu.
"""

# 下周一十二丈
下周 = 12 * 10  # Convert zhang to chi (1丈 = 10尺)

# 高二丈
高 = 2 * 10  # Convert zhang to chi (1丈 = 10尺)

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積尺 = 下周平方 * 高

# 三十六而一
積尺 = Fraction(積尺, 36)

# 程粟一斛，積二尺七寸
一斛積 = 2 + Fraction(7, 10)  # Convert 2尺7寸 to chi (1尺 = 10寸)

# 為粟幾何
粟斛數 = Fraction(積尺, 一斛積)

a = 積尺
b = 粟斛數#----- content ends here -----

"""
"""
