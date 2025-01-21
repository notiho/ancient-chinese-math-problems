"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

"""
Suppose there is a tree 2 zhang in height and 3 chi in circumference. A vine grows at its base, wrapping around the tree 7 times and reaching the top of the tree.
Question: how long is the vine?

The procedure says: Multiply the 7 wraps by 3 chi to obtain the base (股). Use the tree's height as the perpendicular (句). Solve for the hypotenuse (弦), which is the length of the vine.

Answer: the vine is *a* zhang.
"""

from fractions import Fraction
import math

# 木長二丈
木長 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 圍之三尺
圍 = 3

# 葛纏木七周
周數 = 7

# 以七周乘三尺為股
股 = 周數 * 圍

# 木長為句
句 = 木長

# 為之求弦 (弦 = sqrt(股^2 + 句^2))
弦 = math.sqrt(股**2 + 句**2)

# Convert chi back to zhang
a = Fraction(弦, 10)  # 1 zhang = 10 chi
"""
Code error: both arguments should be Rational instances"""
