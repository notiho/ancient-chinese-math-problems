"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a(=305000/3)尺 。
"""

#----- content starts here -----
"""
Suppose there is a square pavilion with a bottom side of 5 zhang, a top side of 4 zhang, and a height of 5 zhang.
Question: what is the volume?

The procedure says: Multiply the bottom side and the top side with each other.
Then, multiply each of them by itself.
Add these together, and multiply by the height.
Finally, divide by 3.

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
下方自乘 = 下方 * 下方
上方自乘 = 上方 * 上方

# 并之
和 = 上下方積 + 下方自乘 + 上方自乘

# 以高乘之
積 = 和 * 高

# 三而一
a = Fraction(積 * 1000, 3) # 305000/3 cubic chi (convert zhang^3 to chi^3)#----- content ends here -----

"""
"""
