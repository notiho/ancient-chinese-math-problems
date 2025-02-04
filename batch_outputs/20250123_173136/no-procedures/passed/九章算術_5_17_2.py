"""
今有圓錐下周三丈五尺，高五丈一尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a cone with a base circumference of 3 zhang 5 chi (35 chi) and a height of 5 zhang 1 chi (51 chi).
Question: what is the volume of the cone?

Answer: the volume is *a* cubic chi.
"""

# 下周 (base circumference) = 3丈5尺 = 35尺
下周 = 35

# 高 (height) = 5丈1尺 = 51尺
高 = 51

# 圓錐的積 (volume of a cone) = (1/3) * 底面積 * 高
# 底面積 (base area) = (下周^2) / (4 * π)
# Approximate π as 3 for simplicity in ancient Chinese calculations

π = 3
底面積 = Fraction(下周**2, 4 * π)

# Calculate the volume
a = Fraction(1, 3) * 底面積 * 高

# Output the result
a
"""
"""
