"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為粟 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground. The base circumference is 12 zhang, and the height is 2 zhang.
Question: What is the volume of the pile, and how much millet does it contain?

The procedure for piled millet says: Multiply the base circumference by itself, then multiply by the height, and divide by 36. 
If the pile leans against a wall, divide by 18. 
If the pile leans against an inner corner, divide by 9.

For millet, 1 hu occupies 2 chi 7 cun of volume. 
For rice, 1 hu occupies 1 chi 6 cun and 1/5 cun of volume. 
For beans, da, hemp, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: The volume is *a* chi, and the millet is *b* hu.
"""

from fractions import Fraction

# 下周一十二丈
下周 = 12  # in zhang

# 高二丈
高 = 2  # in zhang

# Convert zhang to chi (1 zhang = 10 chi)
下周 = 下周 * 10  # in chi
高 = 高 * 10  # in chi

# 下周自乘，以高乘之，三十六而一
積 = (下周 ** 2) * 高 / 36  # in cubic chi

# 程粟一斛，積二尺七寸
# Convert 2 chi 7 cun to cubic chi (1 chi = 10 cun)
一斛積 = 2 + Fraction(7, 10)  # in cubic chi

# 求粟斛數
粟 = 積 / 一斛積  # in hu

# Final results
a = 積  # Volume in cubic chi
b = 粟  # Millet in hu#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 80000/27, Actual: 2962.9629629629626"""
