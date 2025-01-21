"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a(=305000/3)尺 。
"""

"""
Suppose there is a square pavilion with a bottom side of 5 zhang, a top side of 4 zhang, and a height of 5 zhang.
Question: what is the volume?

The procedure says: Multiply the bottom side and the top side with each other.
Then, multiply each of them by itself, and add these together.
Multiply the result by the height, and divide by 3.

Answer: *a*(=305000/3) cubic chi.
"""

# 下方五丈
下方 = 5

# 上方四丈
上方 = 4

# 高五丈
高 = 5

# 上下方相乘
上下方積 = 下方 * 上方

# 又各自乘
下方積 = 下方 * 下方
上方積 = 上方 * 上方

# 并之
總積 = 上下方積 + 下方積 + 上方積

# 以高乘之
體積 = 總積 * 高

# 三而一
a = Fraction(體積, 3) * 10000  # Convert zhang^3 to chi^3 (1 zhang = 10 chi) => 305000/3 cubic chi
"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 3050000/3"""
