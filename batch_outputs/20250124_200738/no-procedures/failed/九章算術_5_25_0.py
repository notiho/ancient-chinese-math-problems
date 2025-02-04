"""
今有盤池，上廣六丈，袤八丈，下廣四丈，袤六丈，深二丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a pond. The top has a width of 6 zhang and a length of 8 zhang. 
The bottom has a width of 4 zhang and a length of 6 zhang. The depth is 2 zhang.
Question: what is the volume of the pond?

Answer: *a* cubic chi.
"""

# Convert all dimensions to chi (1 zhang = 10 chi)
top_width = 6 * 10
top_length = 8 * 10
bottom_width = 4 * 10
bottom_length = 6 * 10
depth = 2 * 10

# Calculate the top area and bottom area
top_area = top_width * top_length
bottom_area = bottom_width * bottom_length

# Use the formula for the volume of a frustum: V = (1/2) * depth * (top_area + bottom_area)
a = Fraction(1, 2) * depth * (top_area + bottom_area)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 212000/3, Actual: 72000"""
