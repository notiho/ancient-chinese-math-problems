"""
今有方亭下方五丈上方四丈高五丈問積幾何
術曰上下方相乘又各自乘并之以高乘之三而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a square pavilion with a bottom square side of 5 zhang, a top square side of 4 zhang, and a height of 5 zhang.
Question: what is the volume?

The procedure says: Multiply the bottom square side and the top square side with each other.
Then, multiply each of them by itself (square them).
Add these results together, and multiply by the height.
Divide by 3 to obtain the volume.

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
下方平方 = 下方 * 下方
上方平方 = 上方 * 上方

# 并之
和 = 上下方積 + 下方平方 + 上方平方

# 以高乘之
積 = 和 * 高

# 三而一
a = Fraction(積, 3) * 100  # Convert from zhang^3 to chi^3 (1 zhang = 10 chi)
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 305000/3, Actual: 30500/3"""
