"""
今有圓困，高一丈三尺三寸、少半寸，容米二千斛。問︰周幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical container with a height of 1 zhang, 3 chi, 3 cun, and half a cun less (1丈3尺2寸5分). 
It can hold 2000 hu of rice. 
Question: what is the circumference of the base?

Answer: the circumference is *a* zhang.
"""

# 高 (height) = 1丈3尺3寸 - 0.5寸
height = 1 * 10 + 3 + Fraction(3, 10) - Fraction(0.5, 10)  # Convert everything to chi

# 容米 (volume) = 2000斛
volume = 2000 * 10  # Convert hu to cubic chi (1 hu = 10 cubic chi)

# Volume of a cylinder: V = π * r^2 * h
# Circumference of the base: 周 = 2 * π * r
# From the volume formula, r^2 = V / (π * h)
# Substituting r into the circumference formula: 周 = 2 * π * sqrt(V / (π * h))

# Simplify the formula for 周:
# 周 = 2 * sqrt(π * V / h)

# Using π ≈ 3 (ancient Chinese approximation):
pi = 3

# Calculate 周
radius_squared = Fraction(volume, pi * height)
radius = radius_squared ** Fraction(1, 2)  # Square root of radius_squared
circumference = 2 * pi * radius

# Convert circumference to zhang
a = Fraction(circumference, 10)  # Convert chi to zhang

a  # The answer is in zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
