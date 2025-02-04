"""
今有圓錐下周三丈五尺，高五丈一尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a cone with a base circumference of 3 zhang 5 chi (35 chi) and a height of 5 zhang 1 chi (51 chi).
Question: what is the volume of the cone?

Answer: *a* cubic chi.
"""

# 下周三丈五尺 (base circumference)
下周 = 35  # in chi

# 高五丈一尺 (height)
高 = 51  # in chi

# 圓錐的積公式 (Volume of a cone): V = (1/3) * base_area * height
# Base area of a circle: A = (C^2) / (4 * π), where C is the circumference

# Using an approximation for π as 3 for simplicity (as was common in ancient Chinese mathematics):
π = 3

# Calculate the base area
底面積 = Fraction(下周**2, 4 * π)

# Calculate the volume of the cone
a = Fraction(1, 3) * 底面積 * 高

# The result is the volume in cubic chi.
"""
"""
