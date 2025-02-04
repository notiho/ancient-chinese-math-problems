"""
今有圓窖，下周二百八十六尺，深三丈六尺。問：受粟幾何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a circular pit with a circumference of 286 chi and a depth of 3 zhang 6 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu.
"""

# 下周 (circumference) = 286 chi
circumference = 286

# 深 (depth) = 3 zhang 6 chi = 3 * 10 + 6 = 36 chi
depth = 36

# Calculate the radius of the circular pit using the formula: circumference = 2 * pi * radius
# Here, we approximate pi as 3 (as was commonly done in ancient Chinese mathematics)
radius = Fraction(circumference, 2 * 3)

# Calculate the area of the circular base: area = pi * radius^2
# Again, using pi = 3
area = 3 * radius * radius

# Calculate the volume of the pit: volume = area * depth
volume = area * depth

# Convert the volume from cubic chi to hu
# 1 hu = 10 cubic chi
a = Fraction(volume, 10)

# Final result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4089800/27, Actual: 122694/5"""
