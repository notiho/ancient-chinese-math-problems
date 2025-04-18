"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a(=4750/9)尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular pavilion with a lower circumference of 3 zhang, an upper circumference of 2 zhang, and a height of 1 zhang.
Question: what is its volume?

The procedure says: Multiply the upper and lower circumferences with each other. 
Then, multiply each circumference by itself. Add these results together.
Multiply the sum by the height. Divide by 36 to obtain the volume.

Answer: *a*(=4750/9) chi³.
"""

from fractions import Fraction

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 上周二丈
上周 = 2 * 10  # Convert zhang to chi

# 高一丈
高 = 1 * 10  # Convert zhang to chi

# 上、下周相乘
上下周積 = 上周 * 下周

# 又各自乘
上周平方 = 上周 * 上周
下周平方 = 下周 * 下周

# 并之
和 = 上下周積 + 上周平方 + 下周平方

# 以高乘之
積 = 和 * 高

# 三十六而一
a = Fraction(積, 36)  # 4750/9 chi³#----- content ends here -----

"""
"""
