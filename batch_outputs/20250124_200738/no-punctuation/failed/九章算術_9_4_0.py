"""
今有木長二丈圍之三尺葛生其下纏木七周上與木齊問葛長幾何
術曰以七周乘三尺為股木長為句為之求弦弦者葛之長
荅曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a tree 2 zhang in height, with a circumference of 3 chi. A vine grows at the base of the tree and wraps around it 7 times, reaching the top of the tree.
Question: how long is the vine?

The procedure says: Multiply the 7 wraps by 3 chi to obtain the base (股). The height of the tree is the perpendicular (句). Use these to calculate the hypotenuse (弦), which is the length of the vine.

The answer says: *a* zhang.
"""

from fractions import Fraction
import math

# 木長二丈
木長 = 2  # in 丈

# 圍之三尺
圍 = 3  # in 尺

# 葛纏木七周
周數 = 7

# 以七周乘三尺為股
股 = 周數 * 圍  # 股 in 尺

# 木長為句
句 = 木長 * 10  # Convert 木長 to 尺 (1 丈 = 10 尺)

# 求弦 (弦 = sqrt(股^2 + 句^2))
弦 = math.sqrt(股**2 + 句**2)

# Convert 弦 back to 丈 (1 丈 = 10 尺)
a = Fraction(弦, 10)  # in 丈#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
