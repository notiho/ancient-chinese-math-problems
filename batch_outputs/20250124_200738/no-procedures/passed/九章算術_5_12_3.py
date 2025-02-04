"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square fortress with a side length of 1 zhang 6 chi and a height of 1 zhang 5 chi.
Question: what is the volume of the fortress?

Answer: the volume is *a* cubic chi.
"""

# 方堡壔邊長 (side length of the square base)
邊長 = 1 * 10 + 6  # 1 zhang = 10 chi, so 1 zhang 6 chi = 16 chi

# 高 (height)
高 = 1 * 10 + 5  # 1 zhang = 10 chi, so 1 zhang 5 chi = 15 chi

# 積 (volume) = base area * height
a = 邊長 * 邊長 * 高  # Volume in cubic chi

a  # Output the result#----- content ends here -----

"""
"""
