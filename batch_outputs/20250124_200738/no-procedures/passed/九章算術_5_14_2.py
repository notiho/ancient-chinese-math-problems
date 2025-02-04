"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square frustum-shaped pavilion (方亭). 
The bottom side is 5 zhang, the top side is 4 zhang, and the height is 5 zhang.
Question: what is the volume of the pavilion?

Answer: *a* cubic chi.
"""

# 下方五丈 (bottom side length in zhang)
下方 = 5

# 上方四丈 (top side length in zhang)
上方 = 4

# 高五丈 (height in zhang)
高 = 5

# Convert zhang to chi (1 zhang = 10 chi)
下方 = 下方 * 10
上方 = 上方 * 10
高 = 高 * 10

# Volume formula for a square frustum: V = (1/3) * 高 * (下方^2 + 下方 * 上方 + 上方^2)
a = Fraction(1, 3) * 高 * (下方**2 + 下方 * 上方 + 上方**2)#----- content ends here -----

"""
"""
