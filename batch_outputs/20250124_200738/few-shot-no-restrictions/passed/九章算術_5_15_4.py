"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular pavilion with a lower circumference of 3 zhang, an upper circumference of 2 zhang, and a height of 1 zhang.
Question: what is the total volume?

The procedure says: Multiply the upper and lower circumferences together, then multiply each of them by itself.
Add these results together, then multiply by the height.
Finally, divide by 36 to obtain the volume.

Answer: *a* chi³.
"""

from fractions import Fraction

# 下周三丈 (lower circumference)
下周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 上周二丈 (upper circumference)
上周 = 2 * 10  # Convert zhang to chi

# 高一丈 (height)
高 = 1 * 10  # Convert zhang to chi

# 上、下周相乘
上下周積 = 上周 * 下周

# 又各自乘 (square each circumference)
下周平方 = 下周 * 下周
上周平方 = 上周 * 上周

# 并之 (add the results)
和 = 上下周積 + 下周平方 + 上周平方

# 以高乘之 (multiply by the height)
體積 = 和 * 高

# 三十六而一 (divide by 36)
a = Fraction(體積, 36)

a  # The volume in chi³#----- content ends here -----

"""
"""
