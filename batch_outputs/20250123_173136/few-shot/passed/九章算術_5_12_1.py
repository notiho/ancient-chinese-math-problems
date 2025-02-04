"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
術曰：方自乘，以高乘之，即積尺。
荅曰： a尺 。
"""

"""
Suppose there is a square fortress with a side length of 1 zhang and 6 chi, and a height of 1 zhang and 5 chi.
Question: what is the volume in cubic chi?

The procedure says: Square the side length (multiply it by itself), then multiply by the height. This gives the volume in cubic chi.

Answer: *a* cubic chi.
"""

# 方一丈六尺
方長 = 1 * 10 + 6  # Convert 1 zhang 6 chi to chi

# 高一丈五尺
高 = 1 * 10 + 5  # Convert 1 zhang 5 chi to chi

# 方自乘
方積 = 方長 * 方長

# 以高乘之，即積尺
a = 方積 * 高
"""
"""
