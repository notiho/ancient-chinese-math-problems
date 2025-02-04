"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a thatched roof (芻甍) with the following dimensions:
- Bottom width: 3 zhang
- Bottom length: 4 zhang
- Top length: 2 zhang (no width at the top)
- Height: 1 zhang

Question: What is the volume of the roof?

Answer: *a* cubic chi.
"""

# Dimensions in zhang
bottom_width = 3  # zhang
bottom_length = 4  # zhang
top_length = 2  # zhang
height = 1  # zhang

# Convert zhang to chi (1 zhang = 10 chi)
bottom_width_chi = bottom_width * 10
bottom_length_chi = bottom_length * 10
top_length_chi = top_length * 10
height_chi = height * 10

# Volume formula for a trapezoidal prism: V = (1/2) * height * (bottom_area + top_area)
# Top area is 0 since there's no width at the top
bottom_area = bottom_width_chi * bottom_length_chi
top_area = 0
volume = Fraction(1, 2) * height_chi * (bottom_area + top_area)

# Final answer
a = volume
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5000, Actual: 6000"""
