"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a(=4750/9)尺 。
"""

"""
Suppose there is a circular pavilion with a lower circumference of 3 zhang, an upper circumference of 2 zhang, and a height of 1 zhang.
Question: what is the volume?

The procedure says: Multiply the upper and lower circumferences with each other. Then, multiply each of them by itself. Add these results together. Multiply the sum by the height. Divide the result by 36.

Answer: *a*(=4750/9) chi³.
"""

from fractions import Fraction

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi

# 上周二丈
上周 = 2 * 10  # Convert zhang to chi

# 高一丈
高 = 1 * 10  # Convert zhang to chi

# 上、下周相乘
上下相乘 = 上周 * 下周

# 又各自乘
下自乘 = 下周 * 下周
上自乘 = 上周 * 上周

# 并之
和 = 上下相乘 + 下自乘 + 上自乘

# 以高乘之
積 = 和 * 高

# 三十六而一
a = Fraction(積, 36)  # 4750/9 chi³
"""
"""
