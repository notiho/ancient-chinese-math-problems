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

# Dimensions of the trench wall
下廣 = 2 * 10  # Convert zhang to chi
袤 = 18 * 10 + 6  # Convert zhang and chi to total chi
高 = 2 * 10 + 5  # Convert zhang and chi to total chi

# Calculate the volume
a = 下廣 * 袤 * 高  # Volume in cubic chi

a  # Output the result#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 46500, Actual: 93000"""
