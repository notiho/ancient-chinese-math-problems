"""
今有井徑五尺，不知其深。立五尺木於井上，從木末望水岸，入徑四寸。問︰井深幾何
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a well with a diameter of 5 chi, but its depth is unknown. A 5-chi-long wooden stick is placed upright at the edge of the well. From the top of the stick, the observer sees the edge of the water, and the line of sight enters the well's diameter by 4 cun.  
Question: how deep is the well?

Answer: the depth of the well is *a* zhang.
"""

# Given values
井徑 = 5  # chi (diameter of the well)
木長 = 5  # chi (length of the wooden stick)
入徑 = Fraction(4, 10)  # chi (4 cun = 4/10 chi)

# The depth of the well forms a right triangle with the radius of the well and the stick's length.
# Using similar triangles:
# 木長 / 井深 = 入徑 / (井徑 / 2)
# Solve for 井深 (well depth):

井深 = 木長 * (井徑 / 2) / 入徑

# Convert the depth to zhang (1 zhang = 10 chi)
a = 井深 / 10

井深, a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 23/4, Actual: 3.125"""
