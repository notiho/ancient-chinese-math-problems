"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為粟 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground. Its base circumference is 12 zhang, and its height is 2 zhang.
Question: what is the volume of the pile, and how much millet does it contain?

The procedure for millet piles says: Multiply the base circumference by itself, then multiply by the height, and divide by 36. 
If the pile is against a wall, divide by 18. If the pile is in a corner, divide by 9.
For millet, 1 hu occupies 2 chi 7 cun. For rice, 1 hu occupies 1 chi 6 cun and 1/5 cun. 
For beans, da, hemp, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun.

Answer: the volume is *a* chi³. It contains *b* hu of millet.
"""

# 下周一十二丈
下周 = 12  # 丈

# 高二丈
高 = 2  # 丈

# 轉換為尺 (1 丈 = 10 尺)
下周 = 下周 * 10
高 = 高 * 10

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 三十六而一
積 = Fraction(積, 36)

# 積二尺七寸 (1 斛 = 2 尺 7 寸 = 27 寸, where 1 尺 = 10 寸)
粟每斛積 = 27  # 寸
粟每斛積 = Fraction(粟每斛積, 10)  # 轉換為尺

# 計算粟的斛數
粟斛數 = Fraction(積, 粟每斛積)

# 結果
a = 積  # 積的體積 (尺³)
b = 粟斛數  # 粟的斛數#----- content ends here -----

"""
"""
