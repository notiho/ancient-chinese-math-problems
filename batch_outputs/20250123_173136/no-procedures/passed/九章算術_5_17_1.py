"""
今有圓錐下周三丈五尺，高五丈一尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a cone with a base circumference of 3 zhang 5 chi (35 chi) and a height of 5 zhang 1 chi (51 chi).
Question: what is the volume of the cone?

Answer: *a* cubic chi.
"""

# 下周 (circumference) = 3丈5尺 = 35尺
下周 = 35

# 高 (height) = 5丈1尺 = 51尺
高 = 51

# 圓錐的積公式：積 = (1/3) * 底面積 * 高
# 底面積公式：底面積 = (周長^2) / (4 * π)
# For simplicity, we approximate π as 3.

# Approximate π
π = 3

# Calculate the radius using the circumference formula: 周長 = 2 * π * 半徑
半徑 = Fraction(下周, 2 * π)

# Calculate the base area: 底面積 = π * 半徑^2
底面積 = π * 半徑**2

# Calculate the volume of the cone: 積 = (1/3) * 底面積 * 高
a = Fraction(1, 3) * 底面積 * 高

a
"""
"""
