"""
今有木長二丈圍之三尺葛生其下纏木七周上與木齊問葛長幾何
術曰以七周乘三尺為股木長為句為之求弦弦者葛之長
荅曰 a丈 
"""

"""
Suppose there is a tree with a height of 2 zhang and a circumference of 3 chi. A vine grows at the base of the tree and wraps around it 7 times, reaching the top of the tree.
Question: how long is the vine?

The procedure says: Multiply the 7 wraps by 3 chi to get the base (股). The height of the tree is the upright (句). Use these to find the hypotenuse (弦), which is the length of the vine.

The answer says: *a* zhang.
"""

from fractions import Fraction
import math

# 木長二丈 (tree height)
木長 = 2  # in 丈

# 圍之三尺 (circumference of the tree)
圍 = 3  # in 尺

# 葛纏木七周 (vine wraps around the tree 7 times)
周數 = 7

# 以七周乘三尺為股 (base = 7 wraps * 3 chi)
股 = 周數 * 圍  # in 尺

# 木長為句 (upright = tree height)
句 = 木長 * 10  # convert 丈 to 尺

# 求弦 (hypotenuse = √(股² + 句²))
弦 = math.sqrt(股**2 + 句**2)

# Convert the result back to 丈
a = Fraction(弦, 10)  # in 丈
"""
Code error: both arguments should be Rational instances"""
