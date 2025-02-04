"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

"""
Suppose there is a square pavilion. The bottom side is 5 zhang, the top side is 4 zhang, and the height is 5 zhang.
Question: what is the volume?

The procedure says: Multiply the bottom side by the top side. Then multiply each side by itself. Add these together. Multiply the result by the height. Divide by 3.

Answer: *a* chi.
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
下方自乘 = 下方 * 下方
上方自乘 = 上方 * 上方

# 并之
總積 = 上下方積 + 下方自乘 + 上方自乘

# 以高乘之
體積 = 總積 * 高

# 三而一
a = Fraction(體積, 3) * 100  # Convert zhang^3 to chi^3 (1 zhang = 10 chi)

"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 30500/3"""
