"""
今有井徑五尺，不知其深。立五尺木於井上，從木末望水岸，入徑四寸。問︰井深幾何
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a well with a diameter of 5 chi, but the depth is unknown. A 5-chi-long wooden stick is placed vertically above the well. From the top of the stick, the observer looks at the edge of the water, and the line of sight enters the well by 4 cun (4/10 of a chi). 
Question: how deep is the well?

Answer: the well is *a* zhang deep.
"""

# Given values
井徑 = 5  # chi (diameter of the well)
木長 = 5  # chi (length of the wooden stick)
入徑 = Fraction(4, 10)  # 4 cun = 4/10 chi (how far the line of sight enters the well)

# The depth of the well can be calculated using similar triangles:
# Depth of the well (井深) / 木長 = 井徑 / 入徑
井深 = 木長 * (井徑 / 入徑)

# Convert depth to zhang (1 zhang = 10 chi)
a = Fraction(井深, 10)  # depth in zhang

a  # Output the depth of the well in zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 23/4, Actual: 25/4"""
