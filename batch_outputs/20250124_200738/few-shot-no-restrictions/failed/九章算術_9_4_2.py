"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a tree 2 zhang in height and 3 chi in circumference. A vine grows at the base of the tree and wraps around it 7 times, reaching the top of the tree.
Question: how long is the vine?

The procedure says: Multiply the 7 wraps by the 3 chi circumference to get the base (股). The height of the tree is the perpendicular (句). Use these to calculate the hypotenuse (弦). The hypotenuse is the length of the vine.

Answer: the vine is *a* zhang long.
"""

from math import sqrt

# 木長 2丈
木長 = 2  # in 丈

# 圍之 3尺
圍 = 3  # in 尺

# Convert 木長 to 尺 (1丈 = 10尺)
木長_in_尺 = 木長 * 10

# 葛纏木 7周
周數 = 7

# 以七周乘三尺為股
股 = 周數 * 圍  # 股 is the base of the triangle

# 木長為句
句 = 木長_in_尺  # 句 is the height of the triangle

# 求弦 (弦 = sqrt(股^2 + 句^2))
弦 = sqrt(股**2 + 句**2)

# Convert 弦 back to 丈 (1丈 = 10尺)
a = 弦 / 10  # 葛長 in 丈

a  # 葛長 in 丈#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 29/10, Actual: 2.9"""
