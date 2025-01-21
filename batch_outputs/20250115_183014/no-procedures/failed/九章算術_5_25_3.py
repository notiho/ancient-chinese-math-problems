"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a pond. The top surface has a width of 6 zhang and a length of 8 zhang. 
The bottom surface has a width of 4 zhang and a length of 6 zhang. The depth of the pond is 2 zhang.
Question: what is the volume of the pond?

Answer: *a* cubic chi.
"""

# Top dimensions
top_width = 6  # in zhang
top_length = 8  # in zhang

# Bottom dimensions
bottom_width = 4  # in zhang
bottom_length = 6  # in zhang

# Depth
depth = 2  # in zhang

# Convert all dimensions to chi (1 zhang = 10 chi)
top_width_chi = top_width * 10
top_length_chi = top_length * 10
bottom_width_chi = bottom_width * 10
bottom_length_chi = bottom_length * 10
depth_chi = depth * 10

# Calculate the area of the top and bottom surfaces
top_area = top_width_chi * top_length_chi
bottom_area = bottom_width_chi * bottom_length_chi

# Calculate the volume using the formula for a truncated prism:
# Volume = (1/2) * depth * (top_area + bottom_area)
a = Fraction(1, 2) * depth_chi * (top_area + bottom_area)

a  # The volume in cubic chi
"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 72000"""
