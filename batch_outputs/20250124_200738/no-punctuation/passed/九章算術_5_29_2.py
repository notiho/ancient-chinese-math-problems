"""
今有委粟平地下周一十二丈高二丈問積及為粟幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為粟 b斛 
"""

#----- content starts here -----
"""
Suppose there is a pile of millet lying flat on the ground. Its circumference is 12 zhang, and its height is 2 zhang.
Question: what is the volume of the pile, and how much millet does it contain?

The procedure for piled millet says: Multiply the circumference by itself, then multiply by the height. Divide by 36 to get the volume.
If the pile leans against a wall, divide by 18.
If the pile is in a corner, divide by 9.
For millet, 1 hu occupies 2 chi 7 cun of volume.
For rice, 1 hu occupies 1 chi 6 cun and 5/10 cun of volume.
For beans, sesame, hemp, or wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: the volume is *a* chi³, and it contains *b* hu of millet.
"""

# 下周一十二丈
周 = 12 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高二丈
高 = 2 * 10  # Convert zhang to chi

# 下周自乘
周平方 = 周 * 周

# 以高乘之
積尺 = 周平方 * 高

# 三十六而一
積尺 = Fraction(積尺, 36)

# 程粟一斛積二尺七寸
一斛積 = 2 + Fraction(7, 10)  # Convert 2 chi 7 cun to chi

# 計算為粟幾何
粟斛 = Fraction(積尺, 一斛積)

# 答案
a = 積尺  # Volume in chi³
b = 粟斛  # Amount of millet in hu#----- content ends here -----

"""
"""
