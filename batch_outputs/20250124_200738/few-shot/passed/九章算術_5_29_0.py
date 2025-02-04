"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為粟 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground, with a base circumference of 12 zhang and a height of 2 zhang.
Question: what is the volume of the pile, and how much millet does it contain?

The procedure for millet piles says: Multiply the base circumference by itself, then multiply by the height, and divide by 36 to get the volume.
If the pile is against a wall, divide by 18. If it is in the inner corner of walls, divide by 9.
For millet, 1 hu corresponds to a volume of 2 chi 7 cun.
For rice, 1 hu corresponds to a volume of 1 chi 6 cun and 1/5 cun.
For beans, da, hemp, and wheat, 1 hu corresponds to a volume of 2 chi 4 cun and 3/10 cun.

Answer: the volume is *a* chi, and it contains *b* hu of millet.
"""

# 下周一十二丈
下周 = 12 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高二丈
高 = 2 * 10  # Convert zhang to chi

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 三十六而一
積 = Fraction(積, 36)

# 程粟一斛，積二尺七寸
一斛積 = 2 + Fraction(7, 10)  # Convert 2 chi 7 cun to chi

# 為粟幾何
b = Fraction(積, 一斛積)

a = 積  # Volume in chi
#----- content ends here -----

"""
"""
