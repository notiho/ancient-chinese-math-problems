"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square pavilion with a bottom side length of 5 zhang, a top side length of 4 zhang, and a height of 5 zhang.
Question: what is the volume?

The procedure says: Multiply the bottom side by itself and the top side by itself.
Add these together, and also add the product of the bottom and top sides.
Then multiply the result by the height.
Finally, divide by 3.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# 下方五丈
下方 = 5  # in 丈

# 上方四丈
上方 = 4  # in 丈

# 高五丈
高 = 5  # in 丈

# 上下方相乘 (上下方各自平方)
下方積 = 下方 * 下方
上方積 = 上方 * 上方

# 又各自乘 (上下方相乘)
上下積 = 下方 * 上方

# 并之 (加總)
總積 = 下方積 + 上方積 + 上下積

# 以高乘之
體積 = 總積 * 高

# 三而一 (除以3)
a = Fraction(體積, 3) * 1000  # Convert from cubic 丈 to cubic 尺 (1 丈 = 10 尺)

a#----- content ends here -----

"""
"""
