"""
今有曲池，上中周二丈，外周四丈，廣一丈，下中周一丈四尺，外周二丈四尺，廣五尺，深一丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a curved pond with the following dimensions:
- Top middle circumference: 2 zhang
- Top outer circumference: 4 zhang
- Top width: 1 zhang
- Bottom middle circumference: 1 zhang 4 chi
- Bottom outer circumference: 2 zhang 4 chi
- Bottom width: 5 chi
- Depth: 1 zhang

Question: What is the total volume of the pond?

Answer: The volume is *a* cubic chi.
"""

# Define the dimensions
top_middle_circumference = 2 * 10  # Convert zhang to chi
top_outer_circumference = 4 * 10  # Convert zhang to chi
top_width = 1 * 10  # Convert zhang to chi

bottom_middle_circumference = 1 * 10 + 4  # Convert zhang and chi
bottom_outer_circumference = 2 * 10 + 4  # Convert zhang and chi
bottom_width = 5  # Already in chi

depth = 1 * 10  # Convert zhang to chi

# Calculate the average circumference
average_circumference = Fraction(
    top_middle_circumference + bottom_middle_circumference, 2
)

# Calculate the average width
average_width = Fraction(top_width + bottom_width, 2)

# Calculate the volume
a = average_circumference * average_width * depth

# The volume is in cubic chi
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5650/3, Actual: 1275"""
