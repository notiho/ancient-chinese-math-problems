"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a tree with a height of 2 zhang and a circumference of 3 chi. A vine grows at the base of the tree, spiraling around it 7 times and reaching the top of the tree. 
Question: how long is the vine?

The procedure says: Multiply the 7 spirals by the 3 chi circumference to obtain the base (股). 
The height of the tree is the perpendicular (句). 
Use these to calculate the hypotenuse (弦), which is the length of the vine.

Answer: the vine is *a* zhang long.
"""

from math import sqrt

# 木長 (tree height) = 2 丈
木長 = 2  # in 丈

# 圍之 (circumference) = 3 尺
圍 = 3  # in 尺

# 葛纏木七周 (7 spirals)
周數 = 7

# 股 = 7周 * 3尺 (convert 尺 to 丈: 10 尺 = 1 丈)
股 = (周數 * 圍) / 10  # 股 in 丈

# 句 = 木長
句 = 木長

# 弦 = sqrt(股^2 + 句^2)
弦 = sqrt(股**2 + 句**2)

# 葛長 (vine length) = 弦
a = 弦  # in 丈

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 29/10, Actual: 2.9"""
