"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a circular pavilion with the following dimensions:
- Bottom circumference: 3 zhang
- Top circumference: 2 zhang
- Height: 1 zhang

Question: What is the volume of the pavilion?

Answer: The volume is *a* chi³.
"""

# Bottom circumference (in chi)
下周 = 3 * 10  # 1 zhang = 10 chi

# Top circumference (in chi)
上周 = 2 * 10  # 1 zhang = 10 chi

# Height (in chi)
高 = 1 * 10  # 1 zhang = 10 chi

# Calculate the radii of the bottom and top circles
# Circumference = 2 * pi * radius -> radius = circumference / (2 * pi)
# Using pi = 3 as per ancient Chinese approximation
下半徑 = Fraction(下周, 2 * 3)
上半徑 = Fraction(上周, 2 * 3)

# Volume of a truncated cone: V = (1/3) * pi * 高 * (r1^2 + r1*r2 + r2^2)
# Using pi = 3
a = Fraction(1, 3) * 3 * 高 * (下半徑**2 + 下半徑 * 上半徑 + 上半徑**2)

# Simplify the result
a = a.limit_denominator()

# The volume is in chi³
a
"""
"""
