"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a circular pavilion with the bottom circumference of 3 zhang, the top circumference of 2 zhang, and a height of 1 zhang.
Question: What is the volume of the pavilion?

Answer: *a* chi.
"""

# 下周三丈 (bottom circumference)
下周 = 3 * 10  # Convert zhang to chi

# 上周二丈 (top circumference)
上周 = 2 * 10  # Convert zhang to chi

# 高一丈 (height)
高 = 1 * 10  # Convert zhang to chi

# Calculate the average radius
# Circumference = 2 * pi * radius, so radius = circumference / (2 * pi)
平均半徑 = Fraction(下周 + 上周, 2) / (2 * Fraction(22, 7))

# Calculate the volume of the frustum
# Volume = (1/3) * pi * height * (r1^2 + r1*r2 + r2^2)
r1 = 下周 / (2 * Fraction(22, 7))  # Bottom radius
r2 = 上周 / (2 * Fraction(22, 7))  # Top radius
a = Fraction(1, 3) * Fraction(22, 7) * 高 * (r1**2 + r1 * r2 + r2**2)

a  # The volume in cubic chi
"""
Variable 'a' has wrong value. Expected: 4750/9, Actual: 16625/33"""
