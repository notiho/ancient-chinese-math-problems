"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a square fortress with a side length of 1 zhang 6 chi and a height of 1 zhang 5 chi.
Question: what is the total volume?

Answer: *a* cubic chi.
"""

# 方堡壔邊長 (side length) = 1丈6尺 = 10尺 + 6尺 = 16尺
邊長 = 10 + 6

# 高 (height) = 1丈5尺 = 10尺 + 5尺 = 15尺
高 = 10 + 5

# Volume = side_length^2 * height
a = 邊長 * 邊長 * 高

a  # The volume in cubic chi
"""
"""
