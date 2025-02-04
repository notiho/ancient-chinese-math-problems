"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a tree 2 zhang tall, with a circumference of 3 chi. A vine grows at the base of the tree, spiraling around it 7 times, and reaches the top of the tree. 
Question: how long is the vine?

The procedure says: Multiply the 7 spirals by the 3 chi circumference to get the base (股). 
The height of the tree is the upright (句). 
Using these, calculate the hypotenuse (弦), which is the length of the vine.

Answer: the vine is *a* zhang long.
"""

from math import sqrt
from fractions import Fraction

# 木長二丈
木長 = 2  # in zhang

# 圍之三尺
圍 = 3  # in chi

# 葛纏木七周
周數 = 7

# 以七周乘三尺為股
股 = 周數 * 圍  # in chi

# 木長為句
句 = 木長 * 10  # convert 木長 to chi (1 zhang = 10 chi)

# 求弦 (弦 = sqrt(股^2 + 句^2))
弦 = sqrt(股**2 + 句**2)

# Convert 弦 back to zhang (1 zhang = 10 chi)
a = Fraction(弦, 10)

a  # The length of the vine in zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
