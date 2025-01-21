"""
今有曲池，上中周二丈，外周四丈，廣一丈，下中周一丈四尺，外周二丈四尺，廣五尺，深一丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a curved pond with the following dimensions:
- The upper middle circumference is 2 zhang, and the outer circumference is 4 zhang, with a width of 1 zhang.
- The lower middle circumference is 1 zhang 4 chi, and the outer circumference is 2 zhang 4 chi, with a width of 5 chi.
- The depth is 1 zhang.

Question: What is the volume of the pond?

Answer: The volume is *a* cubic chi.
"""

# Convert all dimensions to chi for consistency
upper_middle_circumference = 2 * 10  # 2 zhang = 20 chi
upper_outer_circumference = 4 * 10  # 4 zhang = 40 chi
upper_width = 1 * 10  # 1 zhang = 10 chi

lower_middle_circumference = 1 * 10 + 4  # 1 zhang 4 chi = 14 chi
lower_outer_circumference = 2 * 10 + 4  # 2 zhang 4 chi = 24 chi
lower_width = 5  # 5 chi

depth = 1 * 10  # 1 zhang = 10 chi

# Calculate the average middle circumference and average outer circumference
average_middle_circumference = Fraction(upper_middle_circumference + lower_middle_circumference, 2)
average_outer_circumference = Fraction(upper_outer_circumference + lower_outer_circumference, 2)

# Calculate the average width
average_width = Fraction(upper_width + lower_width, 2)

# Calculate the cross-sectional area (average circumference * average width)
cross_sectional_area = average_middle_circumference * average_width

# Calculate the volume (cross-sectional area * depth)
a = cross_sectional_area * depth

a
"""
Variable 'a' has wrong value. Expected: 5650/3, Actual: 1275"""
