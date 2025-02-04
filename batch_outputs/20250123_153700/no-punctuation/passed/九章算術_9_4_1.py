"""
今有木長二丈圍之三尺葛生其下纏木七周上與木齊問葛長幾何
術曰以七周乘三尺為股木長為句為之求弦弦者葛之長
荅曰 a丈 
"""

"""
Suppose there is a tree with a height of 2 zhang and a circumference of 3 chi. A vine grows from the base of the tree and wraps around it 7 times, reaching the top of the tree.
Question: how long is the vine?

The procedure says: Multiply the 7 wraps by the 3 chi circumference to obtain the base (股). The height of the tree is the upright (句). Use these to find the hypotenuse (弦), which is the length of the vine.

The answer says: *a* zhang.
"""

from fractions import Fraction
import math

# 木長二丈
木長 = 2  # in 丈

# 圍之三尺
圍 = Fraction(3, 10)  # Convert 尺 to 丈 (1 丈 = 10 尺)

# 葛纏木七周
周數 = 7

# 以七周乘三尺為股
股 = 周數 * 圍

# 木長為句
句 = 木長

# 求弦 (弦 = sqrt(股^2 + 句^2))
弦 = math.sqrt(float(股**2 + 句**2))

# Convert 弦 back to 丈
a = Fraction(弦).limit_denominator()

a  # 葛長 in 丈
"""
"""
