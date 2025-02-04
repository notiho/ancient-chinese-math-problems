"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為粟 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground. The base circumference is 12 zhang, and the height is 2 zhang.
Question: What is the volume of the pile, and how much millet does it contain?

The procedure for piled millet says: Multiply the base circumference by itself, then multiply by the height, and divide by 36 to get the volume.
If the pile is against a wall, divide by 18. If the pile is in a corner, divide by 9.

For millet, 1 hu occupies 2 chi 7 cun (2.7 chi).
For rice, 1 hu occupies 1 chi 6 cun and 1/5 cun (1.65 chi).
For beans, da, hemp, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun (2.43 chi).

Answer: The volume is *a* chi³. The millet is *b* hu.
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
積 = (下周 ** 2) * 高 / 36  # Volume in cubic chi

# 程粟一斛，積二尺七寸 (1 hu of millet occupies 2.7 chi³)
粟占積 = Fraction(27, 10)  # 2.7 chi³ per hu

# Calculate the amount of millet in hu
粟 = Fraction(積, 粟占積)

# Final results
a = 積  # Volume in cubic chi
b = 粟  # Amount of millet in hu

a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
