"""
今有圓錐下周三丈五尺，高五丈一尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cone with a base circumference of 3 zhang 5 chi and a height of 5 zhang 1 chi.
Question: what is the volume of the cone?

Answer: the volume is *a* cubic chi.
"""

# 圓錐下周三丈五尺 (convert to chi)
周 = 3 * 10 + 5  # 1 zhang = 10 chi

# 高五丈一尺 (convert to chi)
高 = 5 * 10 + 1  # 1 zhang = 10 chi

# Calculate the radius of the base
# Circumference = 2 * pi * radius, so radius = 周 / (2 * pi)
# Use pi = 3 for ancient Chinese calculations
半徑 = Fraction(周, 2 * 3)

# Volume of a cone = (1/3) * pi * r^2 * height
# Use pi = 3 for ancient Chinese calculations
積 = Fraction(1, 3) * 3 * 半徑**2 * 高

# Simplify the result
a = 積

# Output the result
a#----- content ends here -----

"""
"""
