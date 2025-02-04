"""
今有方堡壔方一丈六尺高一丈五尺問積幾何
術曰方自乘以高乘之即積尺
荅曰 a尺 
"""

"""
Suppose there is a square fortress with a side length of 1 zhang and 6 chi, and a height of 1 zhang and 5 chi.
Question: what is the volume in cubic chi?

The procedure says: Square the side length (multiply it by itself), then multiply it by the height. This gives the volume in cubic chi.

Answer: *a* cubic chi.
"""

# 方一丈六尺 (convert to chi: 1 zhang = 10 chi)
方長 = 10 + 6  # 1 zhang 6 chi = 16 chi

# 高一丈五尺 (convert to chi: 1 zhang = 10 chi)
高 = 10 + 5  # 1 zhang 5 chi = 15 chi

# 方自乘
方積 = 方長 * 方長

# 以高乘之
積尺 = 方積 * 高

# 即積尺
a = 積尺
"""
"""
