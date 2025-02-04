"""
今有方錐下方二丈七尺，高二丈九尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a square pyramid with a base side length of 2 zhang 7 chi and a height of 2 zhang 9 chi.
Question: what is the volume of the pyramid?

Answer: the volume is *a* cubic chi.
"""

# 下方 (base side length) = 2丈7尺 = 2 * 10 + 7 = 27尺
base_side = 2 * 10 + 7

# 高 (height) = 2丈9尺 = 2 * 10 + 9 = 29尺
height = 2 * 10 + 9

# Volume of a square pyramid = (1/3) * base_area * height
# Base area = side^2
base_area = base_side * base_side

# Volume
a = Fraction(1, 3) * base_area * height
"""
"""
