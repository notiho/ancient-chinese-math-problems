"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square pavilion with a bottom side of 5 zhang, a top side of 4 zhang, and a height of 5 zhang.
Question: what is the total volume?

The procedure says: Multiply the bottom side by itself, and the top side by itself.
Add these two results together, then multiply by the height.
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

# 上下方相乘，又各自乘
下方積 = 下方**2
上方積 = 上方**2

# 并之
方積和 = 下方積 + 上方積

# 以高乘之
體積 = 方積和 * 高

# 三而一
a = Fraction(體積, 3)

# Convert the result to cubic chi (1 丈 = 10 尺, so 1 cubic 丈 = 1000 cubic chi)
a_in_cubic_chi = a * 1000

a_in_cubic_chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 205/3"""
