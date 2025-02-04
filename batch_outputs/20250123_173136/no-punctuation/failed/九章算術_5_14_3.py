"""
今有方亭下方五丈上方四丈高五丈問積幾何
術曰上下方相乘又各自乘并之以高乘之三而一
荅曰 a尺 
"""

"""
Suppose there is a square pavilion with a bottom square side of 5 zhang, a top square side of 4 zhang, and a height of 5 zhang.
Question: what is the volume?

The procedure says: Multiply the bottom square side by itself, and the top square side by itself.
Add these results together. Then multiply by the height.
Divide the result by 3 to obtain the volume.

Answer: *a* chi.
"""

# 下方五丈
下方 = 5

# 上方四丈
上方 = 4

# 高五丈
高 = 5

# 上下方相乘，又各自乘
下方積 = 下方 * 下方
上方積 = 上方 * 上方

# 并之
方積和 = 下方積 + 上方積

# 以高乘之
體積 = 方積和 * 高

# 三而一
a = Fraction(體積, 3) * 100  # Convert zhang^3 to chi^3 (1 zhang = 10 chi)

"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 20500/3"""
