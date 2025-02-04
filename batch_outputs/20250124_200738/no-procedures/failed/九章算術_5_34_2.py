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

# Convert height to chi (1丈 = 10尺, 1尺 = 10寸, 1寸 = 10分)
height = 10 + 3 + Fraction(3 * 10 - 5, 10)  # 1丈3尺2寸5分 in chi

# Volume of the cylinder in cubic chi (1斛 = 10斗, 1斗 = 10升, 1升 = 1立方尺)
volume = 2000 * 10 * 10  # 2000斛 in cubic chi

# Volume of a cylinder: V = π * r^2 * h
# Rearrange to find r^2: r^2 = V / (π * h)
# Use π ≈ 3 for ancient Chinese calculations
pi = 3
radius_squared = Fraction(volume, pi * height)

# Circumference of the base: C = 2 * π * r
# r = sqrt(radius_squared), so C = 2 * π * sqrt(radius_squared)
# Approximate sqrt(radius_squared) using ancient methods: sqrt(x) ≈ x^(1/2)
# Circumference = 2 * π * sqrt(radius_squared)
circumference = 2 * pi * radius_squared**(1/2)

# Convert circumference to zhang (1丈 = 10尺)
a = Fraction(circumference, 10)  # Convert chi to zhang

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
