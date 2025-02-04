"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為粟 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground. The base circumference is 12 zhang, and the height is 2 zhang.
Question: what is the volume, and how much millet does it contain?

The procedure for piled millet says: Square the base circumference, multiply by the height, and divide by 36 to get the volume.
If the pile is against a wall, divide by 18 instead.
If the pile is in the inner corner of walls, divide by 9 instead.
For millet, 1 hu occupies 2 chi 7 cun of volume.
For rice, 1 hu occupies 1 chi 6 cun and 1/5 cun of volume.
For beans, da, hemp, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: the volume is *a* chi³. It contains *b* hu of millet.
"""

from fractions import Fraction

# 下周一十二丈
下周 = 12  # in zhang

# 高二丈
高 = 2  # in zhang

# Convert zhang to chi (1 zhang = 10 chi)
下周 = 下周 * 10  # in chi
高 = 高 * 10  # in chi

# 委粟術曰：下周自乘，以高乘之，三十六而一
積 = (下周 ** 2) * 高 / 36  # in chi³

# 程粟一斛，積二尺七寸
# Convert 2 chi 7 cun to chi (1 chi = 10 cun)
一斛積 = 2 + Fraction(7, 10)  # in chi³

# 求粟斛數
粟斛數 = Fraction(積, 一斛積)

# Final answers
a = 積  # Volume in chi³
b = 粟斛數  # Amount of millet in hu

# Output results
a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
