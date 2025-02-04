"""
今有塹堵下廣二丈，袤一十八丈六尺，高二丈五尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a trench wall with the following dimensions:
- Bottom width: 2 zhang
- Length: 18 zhang 6 chi
- Height: 2 zhang 5 chi

Question: What is the total volume?

Answer: The volume is *a* cubic chi.
"""

# Convert all dimensions to chi (1 zhang = 10 chi)
bottom_width = 2 * 10  # 2 zhang = 20 chi
length = 18 * 10 + 6  # 18 zhang 6 chi = 186 chi
height = 2 * 10 + 5  # 2 zhang 5 chi = 25 chi

# Calculate the volume (width × length × height)
a = bottom_width * length * height  # in cubic chi

# The result is stored in `a`.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 46500, Actual: 93000"""
