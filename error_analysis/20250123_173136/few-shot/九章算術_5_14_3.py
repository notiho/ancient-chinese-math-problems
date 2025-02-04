"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a尺 。
"""

"""
Suppose there is a square pavilion with a lower base of 5 zhang, an upper base of 4 zhang, and a height of 5 zhang.
Question: what is the total volume?

The procedure says: Multiply the upper and lower bases with each other. Then, multiply each base by itself. Add these together. Multiply the result by the height, and divide by 3.

Answer: *a* chi.
"""

# 下方五丈
下方 = 5

# 上方四丈
上方 = 4

# 高五丈
高 = 5

# 上下方相乘
上下相乘 = 上方 * 下方

# 又各自乘
下方自乘 = 下方 * 下方
上方自乘 = 上方 * 上方

# 并之
和 = 上下相乘 + 下方自乘 + 上方自乘

# 以高乘之
積 = 和 * 高

# 三而一
#ERR: unit conversion
#a = Fraction(積, 3) * 10  # Convert zhang to chi (1 zhang = 10 chi)
a = Fraction(積, 3) * 1000  # Convert zhang to chi (1 zhang = 10 chi)
"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 3050/3"""
