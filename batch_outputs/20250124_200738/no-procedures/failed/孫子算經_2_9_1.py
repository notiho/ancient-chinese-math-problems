"""
今有圓窖，下周二百八十六尺，深三丈六尺。問：受粟幾何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a circular pit with a circumference of 286 chi at the bottom and a depth of 3 zhang 6 chi.
Question: how much millet can it hold?

Answer: it can hold *a* hu.
"""

# 下周二百八十六尺 (circumference of the circular pit)
circumference = 286

# 深三丈六尺 (depth of the pit)
depth = 3 * 10 + 6  # 1 zhang = 10 chi

# Calculate the radius of the circular pit
# Circumference = 2 * π * radius
# Using π = 3 (ancient Chinese approximation)
radius = Fraction(circumference, 2 * 3)

# Calculate the volume of the pit (cylinder volume formula: π * r^2 * h)
# Using π = 3
volume = 3 * radius**2 * depth

# Convert the volume from cubic chi to hu
# 1 hu = 10 cubic chi
a = Fraction(volume, 10)  # Convert to hu

a  # The amount of millet the pit can hold in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4089800/27, Actual: 122694/5"""
