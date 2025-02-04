"""
今有井徑五尺，不知其深。立五尺木於井上，從木末望水岸，入徑四寸。問︰井深幾何
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a well with a diameter of 5 chi, but the depth is unknown. A 5 chi long wooden stick is placed upright at the edge of the well. From the top of the stick, the observer sees the edge of the water, and the line of sight enters the well's diameter by 4 cun (1 chi = 10 cun).
Question: how deep is the well?

Answer: the well is *a* zhang deep (1 zhang = 10 chi).
"""

# Given values
井徑 = 5  # chi
木高 = 5  # chi
入徑 = Fraction(4, 10)  # chi (convert 4 cun to chi)

# The depth of the well can be calculated using similar triangles.
# The ratio of the depth of the well to the diameter of the well (minus the offset) is equal to the ratio of the height of the stick to the offset.

井深 = 木高 * (井徑 / 入徑 - 1)

# Convert depth to zhang
a = Fraction(井深, 10)  # Convert chi to zhang

井深, a#----- content ends here -----

"""
"""
