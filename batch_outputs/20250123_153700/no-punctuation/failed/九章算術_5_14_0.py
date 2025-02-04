"""
今有方亭下方五丈上方四丈高五丈問積幾何
術曰上下方相乘又各自乘并之以高乘之三而一
荅曰 a尺 
"""

"""
Suppose there is a square pavilion with a bottom square side of 5 zhang, a top square side of 4 zhang, and a height of 5 zhang.
Question: what is the volume?

The procedure says: Multiply the bottom square side by the top square side.
Then, multiply each square side by itself and add these.
Multiply the result by the height.
Finally, divide by 3.

The answer says: *a* chi.
"""

# 下方五丈
下方 = 5

# 上方四丈
上方 = 4

# 高五丈
高 = 5

# 上下方相乘
上下相乘 = 下方 * 上方

# 又各自乘
下方自乘 = 下方 * 下方
上方自乘 = 上方 * 上方

# 并之
并之 = 上下相乘 + 下方自乘 + 上方自乘

# 以高乘之
以高乘之 = 并之 * 高

# 三而一
a = Fraction(以高乘之, 3) * 100  # Convert zhang to chi (1 zhang = 10 chi)
"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 30500/3"""
