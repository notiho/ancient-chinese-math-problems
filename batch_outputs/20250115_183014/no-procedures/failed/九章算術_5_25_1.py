"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a pond. The top surface has a width of 6 zhang and a length of 8 zhang. 
The bottom surface has a width of 4 zhang and a length of 6 zhang. The depth is 2 zhang.
Question: what is the volume of the pond?

Answer: *a* cubic chi.
"""

# Convert zhang to chi (1 zhang = 10 chi)
top_width = 6 * 10
top_length = 8 * 10
bottom_width = 4 * 10
bottom_length = 6 * 10
depth = 2 * 10

# Calculate the area of the top and bottom surfaces
top_area = top_width * top_length
bottom_area = bottom_width * bottom_length

# Use the formula for the volume of a truncated prism: V = (1/2) * depth * (top_area + bottom_area)
a = Fraction(1, 2) * depth * (top_area + bottom_area)

# The result is in cubic chi.
"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 72000"""
