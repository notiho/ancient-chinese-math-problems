"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
答曰： a 方。
"""

#----- content starts here -----
"""
Suppose there is a dike (堤) with the following dimensions:
- Bottom width: 5 zhang
- Top width: 3 zhang
- Height: 2 zhang
- Length: 60 chi

We want to calculate the total volume of the dike in cubic chi (方) and determine how many blocks of 1000 cubic chi can be made.

Answer: *a* blocks.
"""

# Dimensions of the dike
下廣 = 5 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上廣 = 3 * 10  # Convert zhang to chi
高 = 2 * 10    # Convert zhang to chi
長 = 60        # Length in chi

# Calculate the cross-sectional area (trapezoid formula: (top width + bottom width) * height / 2)
截面積 = (上廣 + 下廣) * 高 / 2

# Calculate the total volume (cross-sectional area * length)
總體積 = 截面積 * 長

# Calculate how many blocks of 1000 cubic chi can be made
a = 總體積 // 1000  # Integer division to find the number of full blocks

# Output the result
a#----- content ends here -----

"""
"""
