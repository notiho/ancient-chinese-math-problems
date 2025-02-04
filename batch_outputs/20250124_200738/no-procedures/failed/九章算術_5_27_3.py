"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a valley with the following dimensions:
- Top width: 2 zhang
- Top length: 7 zhang
- Bottom width: 8 chi
- Bottom length: 4 zhang
- Depth: 6 zhang 5 chi

Question: What is the total volume of the valley?

Answer: The volume is *a* cubic chi.
"""

# Convert all dimensions to chi (1 zhang = 10 chi)
top_width = 2 * 10  # 2 zhang = 20 chi
top_length = 7 * 10  # 7 zhang = 70 chi
bottom_width = 8  # 8 chi
bottom_length = 4 * 10  # 4 zhang = 40 chi
depth = 6 * 10 + 5  # 6 zhang 5 chi = 65 chi

# Calculate the average width and length
average_width = (top_width + bottom_width) / 2
average_length = (top_length + bottom_length) / 2

# Calculate the volume (average width * average length * depth)
a = Fraction(average_width * average_length * depth)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 52000, Actual: 50050"""
