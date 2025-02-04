"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular pavilion with a lower circumference of 3 zhang, an upper circumference of 2 zhang, and a height of 1 zhang.
Question: what is the volume?

The procedure says: Multiply the upper and lower circumferences with each other, then multiply each circumference by itself. Add these results together, then multiply by the height. Finally, divide by 36 to get the volume.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# 下周三丈 (convert to chi: 1丈 = 10尺)
下周 = 3 * 10  # in chi

# 上周二丈 (convert to chi: 1丈 = 10尺)
上周 = 2 * 10  # in chi

# 高一丈 (convert to chi: 1丈 = 10尺)
高 = 1 * 10  # in chi

# 上、下周相乘
上下周積 = 上周 * 下周

# 又各自乘 (square each circumference)
下周平方 = 下周 * 下周
上周平方 = 上周 * 上周

# 并之 (add the results)
和 = 上下周積 + 下周平方 + 上周平方

# 以高乘之 (multiply by the height)
積 = 和 * 高

# 三十六而一 (divide by 36)
a = Fraction(積, 36)

# Output the result
a#----- content ends here -----

"""
"""
