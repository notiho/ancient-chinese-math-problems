"""
今有井徑五尺，不知其深。立五尺木於井上，從木末望水岸，入徑四寸。問︰井深幾何
荅曰： a丈 。
"""

"""
Suppose there is a well with a diameter of 5 chi (尺). The depth of the well is unknown.
A 5-chi-long wooden pole is placed vertically above the well. From the top of the pole, the observer sees the edge of the water at a point 4 cun (寸) inside the well's diameter.
Question: how deep is the well?

Answer: the well is *a* zhang (丈) deep.
"""

# Constants
井徑 = 5  # Well diameter in chi
木長 = 5  # Length of the wooden pole in chi
入徑 = Fraction(4, 10)  # The distance inside the well's diameter in chi (4 cun = 4/10 chi)

# The radius of the well
井半徑 = 井徑 / 2

# Using similar triangles:
# Depth of the well (井深) / Radius of the well (井半徑) = Length of the pole (木長) / Distance inside the well's diameter (入徑)
井深 = (木長 * 井半徑) / 入徑

# Convert depth to zhang (1 zhang = 10 chi)
a = 井深 / 10

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 23/4, Actual: 3.125"""
