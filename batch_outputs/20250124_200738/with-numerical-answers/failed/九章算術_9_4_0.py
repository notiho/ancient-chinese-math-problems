"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a(=29/10)丈 。
"""

#----- content starts here -----
"""
Suppose there is a tree 2 zhang in height, with a circumference of 3 chi. A vine grows at the base of the tree, spiraling around it 7 times and reaching the top of the tree.
Question: how long is the vine?

The procedure says: Multiply the 7 spirals by the 3 chi circumference to obtain the base (股). Use the tree's height as the upright (句). Solve for the hypotenuse (弦), which is the length of the vine.

Answer: *a*(=29/10) zhang.
"""

from fractions import Fraction
import math

# 木長二丈
木長 = 2  # in 丈

# 圍之三尺
圍 = Fraction(3, 10)  # convert 尺 to 丈 (1 丈 = 10 尺)

# 葛纏木七周
周數 = 7

# 以七周乘三尺為股
股 = 周數 * 圍

# 木長為句
句 = 木長

# 為之求弦 (弦 = sqrt(股^2 + 句^2))
弦平方 = 股**2 + 句**2
弦 = Fraction(math.sqrt(弦平方))

a = 弦  # 29/10 丈#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 29/10, Actual: 6530219459687219/2251799813685248"""
