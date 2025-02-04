"""
今有垣下廣三尺，上廣二尺，高一丈二尺，袤二十二丈五尺八寸。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall with the following dimensions:
- Bottom width: 3 chi
- Top width: 2 chi
- Height: 1 zhang 2 chi (12 chi)
- Length: 22 zhang 5 chi 8 cun (225.8 chi)

Question: What is the total volume of the wall?

Answer: The volume is *a* cubic chi.
"""

# Dimensions
bottom_width = 3  # chi
top_width = 2  # chi
height = 12  # chi (1 zhang = 10 chi, so 1 zhang 2 chi = 12 chi)
length = 225 + Fraction(8, 10)  # chi (22 zhang 5 chi 8 cun = 225.8 chi)

# Average width (since the wall tapers from bottom to top)
average_width = Fraction(bottom_width + top_width, 2)

# Volume formula: Volume = average_width * height * length
a = average_width * height * length

a  # The total volume in cubic chi#----- content ends here -----

"""
"""
