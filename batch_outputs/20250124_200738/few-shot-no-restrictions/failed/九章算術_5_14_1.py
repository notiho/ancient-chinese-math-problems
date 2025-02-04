"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square pavilion with a bottom side length of 5 zhang, a top side length of 4 zhang, and a height of 5 zhang.
Question: what is the total volume?

The procedure says: Multiply the bottom side by itself, and the top side by itself. Add these together.
Then multiply by the height, and divide by 3.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# 下方五丈
下方 = 5  # in 丈

# 上方四丈
上方 = 4  # in 丈

# 高五丈
高 = 5  # in 丈

# 上下方相乘，又各自乘
下方積 = 下方 ** 2
上方積 = 上方 ** 2

# 并之
合積 = 下方積 + 上方積

# 以高乘之
體積_丈 = 合積 * 高

# 三而一
體積_丈 = Fraction(體積_丈, 3)

# Convert from cubic 丈 to cubic 尺 (1 丈 = 10 尺, so 1 cubic 丈 = 1000 cubic 尺)
體積_尺 = 體積_丈 * 1000

a = 體積_尺
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 205000/3"""
