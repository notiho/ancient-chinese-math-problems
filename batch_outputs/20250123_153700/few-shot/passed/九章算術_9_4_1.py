"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

"""
Suppose there is a tree 2 zhang in height, with a circumference of 3 chi. A vine grows at its base, wrapping around the tree 7 times and reaching the top of the tree.
Question: how long is the vine?

The procedure says: Multiply the 7 wraps by the 3 chi circumference to get the base (股). Use the tree's height as the perpendicular (句). Use these to find the hypotenuse (弦). The hypotenuse is the length of the vine.

Answer: the vine is *a* zhang long.
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

# 為之求弦 (弦 = sqrt(股^2 + 句^2))
弦 = math.sqrt(float(股**2 + 句**2))

# Convert result back to 丈
a = Fraction(弦).limit_denominator()

"""
"""
