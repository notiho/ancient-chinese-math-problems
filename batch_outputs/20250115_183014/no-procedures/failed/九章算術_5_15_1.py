"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a circular pavilion with the bottom circumference of 3 zhang, the top circumference of 2 zhang, and a height of 1 zhang.
Question: what is the volume of the pavilion?

Answer: the volume is *a* cubic chi.
"""

# 下周 (bottom circumference) = 3 丈
下周 = 3 * 10  # Convert zhang to chi

# 上周 (top circumference) = 2 丈
上周 = 2 * 10  # Convert zhang to chi

# 高 (height) = 1 丈
高 = 1 * 10  # Convert zhang to chi

# Use the formula for the volume of a truncated cone:
# V = (1/12) * 高 * (下周^2 + 下周 * 上周 + 上周^2)

a = Fraction(1, 12) * 高 * (下周**2 + 下周 * 上周 + 上周**2)  # Volume in cubic chi

a  # Output the result
"""
Variable 'a' has wrong value. Expected: 4750/9, Actual: 4750/3"""
