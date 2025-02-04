"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
答曰： a 方。
"""

"""
Suppose there is a dike (堤) with the following dimensions:
- Bottom width: 5 zhang
- Top width: 3 zhang
- Height: 2 zhang
- Length: 60 chi

It is desired to calculate the volume of the dike in cubic chi, and then determine how many cubic blocks of 1000 cubic chi each can be made.

Answer: *a* blocks.
"""

# Dimensions of the dike
下廣 = 5 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上廣 = 3 * 10  # Convert zhang to chi
高 = 2 * 10    # Convert zhang to chi
長 = 60        # Length is already in chi

# Volume of the dike (trapezoidal prism formula: V = (1/2) * (bottom_width + top_width) * height * length)
體積 = Fraction(1, 2) * (下廣 + 上廣) * 高 * 長

# Calculate how many blocks of 1000 cubic chi can be made
a = 體積 // 1000  # Integer division to find the number of full blocks

a
"""
"""
