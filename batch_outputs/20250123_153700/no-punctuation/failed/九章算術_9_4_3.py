"""
今有木長二丈圍之三尺葛生其下纏木七周上與木齊問葛長幾何
術曰以七周乘三尺為股木長為句為之求弦弦者葛之長
荅曰 a丈 
"""

"""
Suppose there is a tree 2 zhang tall, with a circumference of 3 chi. A vine grows from the base of the tree, wrapping around it 7 times and reaching the top of the tree.
Question: how long is the vine?

The procedure says: Multiply the 7 turns by the 3 chi, obtaining the base (股). The height of the tree is the upright (句). Use these to find the hypotenuse (弦). The hypotenuse is the length of the vine.

Answer: the vine is *a* zhang long.
"""

from fractions import Fraction
import math

# 木長二丈
木長 = 2  # in zhang

# 圍之三尺
圍 = 3  # in chi

# 葛纏木七周
周數 = 7

# 以七周乘三尺，為股
股 = 周數 * 圍  # in chi

# 木長為句
句 = 木長 * 10  # convert 木長 to chi (1 zhang = 10 chi)

# 求弦 (弦 = sqrt(股^2 + 句^2))
弦 = math.sqrt(股**2 + 句**2)  # in chi

# Convert 弦 back to zhang
a = Fraction(弦, 10)  # in zhang
"""
Code error: both arguments should be Rational instances"""
