"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
術曰：上下方相乘，又各自乘，并之，以高乘之，三而一。
荅曰： a(=305000/3)尺 。
"""

#----- content starts here -----
"""
Suppose there is a square pavilion with a lower side of 5 zhang, an upper side of 4 zhang, and a height of 5 zhang.
Question: what is the volume?

The procedure says: Multiply the upper and lower sides with each other, then multiply each of them by itself.
Add these results together, and multiply by the height.
Finally, divide by 3.

Answer: *a*(=305000/3) cubic chi.
"""

# 下方五丈
下方 = 5

# 上方四丈
上方 = 4

# 高五丈
高 = 5

# 將單位轉換為尺 (1丈 = 10尺)
下方 = 下方 * 10
上方 = 上方 * 10
高 = 高 * 10

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
a = Fraction(積, 3) # 305000/3 cubic chi#----- content ends here -----

"""
"""
