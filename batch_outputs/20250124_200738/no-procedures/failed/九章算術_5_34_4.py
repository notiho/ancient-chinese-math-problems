"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical container with a height of 1 zhang, 3 chi, 3 cun, and half a cun (1丈3尺3寸少半寸). It can hold 2000 hu of rice.
Question: what is the circumference of the base?

Answer: the circumference is *a* zhang.
"""

# Height of the cylinder in chi
height = 10 + 3 + Fraction(3, 10) - Fraction(1, 20)  # 1丈 = 10尺, 3尺, 3寸 = 3/10尺, 少半寸 = -1/20尺

# Volume of the cylinder in cubic chi
volume = 2000 * 10  # 1斛 = 10立方尺

# Formula for the volume of a cylinder: V = π * r^2 * h
# Rearrange to find the radius: r = sqrt(V / (π * h))
# Circumference: C = 2 * π * r

# Using π ≈ 3 for ancient Chinese calculations
pi = 3

# Solve for the radius
radius_squared = Fraction(volume, pi * height)
radius = radius_squared ** Fraction(1, 2)

# Solve for the circumference
circumference = 2 * pi * radius

# Convert circumference to zhang
a = Fraction(circumference, 10)  # 1丈 = 10尺

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
