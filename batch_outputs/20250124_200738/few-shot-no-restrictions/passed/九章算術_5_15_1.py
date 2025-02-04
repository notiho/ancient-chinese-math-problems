"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular pavilion with a bottom circumference of 3 zhang, a top circumference of 2 zhang, and a height of 1 zhang.
Question: what is the total volume?

The procedure says: Multiply the top and bottom circumferences with each other. Then, multiply each circumference by itself. Add these together. Multiply the result by the height. Finally, divide by 36.

Answer: *a* chi³.
"""

from fractions import Fraction

# 下周三丈 (bottom circumference)
下周 = 3  # in zhang

# 上周二丈 (top circumference)
上周 = 2  # in zhang

# 高一丈 (height)
高 = 1  # in zhang

# Convert zhang to chi (1 zhang = 10 chi)
下周 *= 10
上周 *= 10
高 *= 10

# 上、下周相乘
上下周積 = 上周 * 下周

# 又各自乘 (square each circumference)
下周平方 = 下周 * 下周
上周平方 = 上周 * 上周

# 并之 (add them together)
和 = 上下周積 + 下周平方 + 上周平方

# 以高乘之 (multiply by the height)
積 = 和 * 高

# 三十六而一 (divide by 36)
a = Fraction(積, 36)

# Output the result
a#----- content ends here -----

"""
"""
