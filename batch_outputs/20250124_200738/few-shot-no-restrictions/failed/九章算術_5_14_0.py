"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square pavilion with a bottom side length of 5 zhang, a top side length of 4 zhang, and a height of 5 zhang.
Question: what is the volume?

The procedure says: Multiply the bottom side length by itself, and the top side length by itself.
Add these two results together, then multiply by the height.
Finally, divide by 3 to get the volume.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# 下方五丈 (convert to chi: 1 zhang = 10 chi)
下方 = 5 * 10

# 上方四丈 (convert to chi: 1 zhang = 10 chi)
上方 = 4 * 10

# 高五丈 (convert to chi: 1 zhang = 10 chi)
高 = 5 * 10

# 上下方相乘 (square the side lengths)
下方積 = 下方 ** 2
上方積 = 上方 ** 2

# 又各自乘，并之
總積 = 下方積 + 上方積

# 以高乘之
體積 = 總積 * 高

# 三而一 (divide by 3)
a = Fraction(體積, 3)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 205000/3"""
