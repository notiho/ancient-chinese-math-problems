"""
今有委粟平地下周一十二丈高二丈問積及為粟幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為粟 b斛 
"""

#----- content starts here -----
"""
Suppose there is a pile of millet lying flat on the ground, with a circumference of 12 zhang and a height of 2 zhang.
Question: What is the volume of the pile, and how much millet does it contain?

The procedure for piled millet says: Multiply the circumference by itself, then multiply by the height.
Divide by 36 to get the volume for a free-standing pile.
For a pile leaning against a wall, divide by 18.
For a pile in a corner, divide by 9.
For millet, 1 hu occupies 2 chi 7 cun of volume.
For rice, 1 hu occupies 1 chi 6 cun and 5/10 cun of volume.
For beans, sesame, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: The volume is *a* chi³, and it contains *b* hu of millet.
"""

# 周一十二丈
周 = 12 * 10  # Convert zhang to chi

# 高二丈
高 = 2 * 10  # Convert zhang to chi

# 下周自乘
周平方 = 周 * 周

# 以高乘之
積 = 周平方 * 高

# 三十六而一
積 = Fraction(積, 36)

# 積為 a 尺³
a = 積

# 程粟一斛積二尺七寸
粟一斛積 = 2 + Fraction(7, 10)  # Convert 2 chi 7 cun to chi³

# 為粟 b 斛
b = Fraction(積, 粟一斛積)#----- content ends here -----

"""
"""
