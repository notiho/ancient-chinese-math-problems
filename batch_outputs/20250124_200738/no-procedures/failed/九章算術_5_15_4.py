"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular pavilion with the bottom circumference of 3 zhang, the top circumference of 2 zhang, and a height of 1 zhang.
Question: what is the volume of the pavilion?

Answer: it is *a* cubic chi.
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

# Calculate the volume using the formula for a truncated cone: V = (1/3) * pi * h * (r1^2 + r1*r2 + r2^2)
# Here, r1 and r2 are the radii of the bottom and top circles, and h is the height.
下半徑 = 下周 / (2 * Fraction(22, 7))
上半徑 = 上周 / (2 * Fraction(22, 7))

a = Fraction(1, 3) * Fraction(22, 7) * 高 * (下半徑**2 + 下半徑 * 上半徑 + 上半徑**2)

# The result `a` is in cubic chi.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4750/9, Actual: 16625/33"""
