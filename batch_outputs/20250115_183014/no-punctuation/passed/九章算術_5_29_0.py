"""
今有委粟平地下周一十二丈高二丈問積及為粟幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為粟 b斛 
"""

"""
Suppose there is a pile of millet on flat ground. The circumference of its base is 12 zhang, and its height is 2 zhang.
Question: what is the volume of the pile, and how many hu of millet does it contain?

The procedure for piled millet says: Multiply the circumference of the base by itself, then multiply by the height.
Divide by 36 to get the volume.
If the pile leans against a wall, divide by 18.
If the pile is in a corner against two walls, divide by 9.
For millet, 1 hu occupies 2 chi 7 cun of volume.

Answer: the volume is *a* chi³, and it contains *b* hu of millet.
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

# 程粟一斛積二尺七寸
一斛積 = 2 + Fraction(7, 10)  # Convert 2 chi 7 cun to chi

# 積除以一斛積，得粟數
粟數 = Fraction(積, 一斛積)

a = 積  # Volume in chi³
b = 粟數  # Amount of millet in hu
"""
"""
