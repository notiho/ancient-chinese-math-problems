"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

"""

"""


from fractions import Fraction
import math

# 木長二丈
木長 = 2  # 丈

# 圍之三尺
圍 = 3  # 尺

# 葛纏木七周
周數 = 7

# 以七周乘三尺為股
股 = 周數 * 圍  # 股的長度（尺）

# 木長為句
句 = 木長 * 10  # 句的長度（轉換為尺）

# 為之求弦
# 弦 = sqrt(股^2 + 句^2)
弦 = math.sqrt(股**2 + 句**2)

# 弦者，葛之長（轉換為丈）
a = Fraction(弦, 10)  # 將弦轉換回丈


"""

"""


"""
Code error: both arguments should be Rational instances"""
