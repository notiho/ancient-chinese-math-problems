"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a tree 2 zhang in height and 3 chi in circumference.
A vine grows at the base of the tree, spiraling around it 7 times and reaching the top of the tree.
Question: how long is the vine?

The procedure says: Multiply the 7 spirals by the 3 chi circumference to obtain the base (股).
Take the tree's height as the upright (句).
Use these to calculate the hypotenuse (弦), which is the length of the vine.

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

# 為之求弦
弦平方 = 股**2 + 句**2  # 弦^2 = 股^2 + 句^2
弦 = math.sqrt(弦平方)  # 弦 in 尺

# Convert 弦 back to 丈 (1 丈 = 10 尺)
a = Fraction(弦, 10)
#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
