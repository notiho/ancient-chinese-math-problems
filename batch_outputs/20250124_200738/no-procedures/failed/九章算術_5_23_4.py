"""
今有芻童，下廣二丈，袤三丈，上廣三丈，袤四丈，高三丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a haystack (芻童) with the following dimensions:
- Bottom width: 2 zhang
- Bottom length: 3 zhang
- Top width: 3 zhang
- Top length: 4 zhang
- Height: 3 zhang

Question: What is the volume of the haystack?

Answer: The volume is *a* cubic chi.
"""

# Convert zhang to chi (1 zhang = 10 chi)
bottom_width = 2 * 10  # in chi
bottom_length = 3 * 10  # in chi
top_width = 3 * 10  # in chi
top_length = 4 * 10  # in chi
height = 3 * 10  # in chi

# Formula for the volume of a frustum:
# V = (H / 3) * (A1 + A2 + sqrt(A1 * A2))
# where:
# H = height
# A1 = area of the bottom
# A2 = area of the top

# Calculate the areas of the bottom and top
A1 = bottom_width * bottom_length  # bottom area in square chi
A2 = top_width * top_length  # top area in square chi

# Calculate the volume
a = Fraction(height, 3) * (A1 + A2 + Fraction((A1 * A2) ** 0.5))

# Final volume in cubic chi
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26500, Actual: 29120874835894425/1099511627776"""
