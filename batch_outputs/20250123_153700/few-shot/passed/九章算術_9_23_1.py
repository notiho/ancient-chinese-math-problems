"""
今有井徑五尺，不知其深。立五尺木於井上，從木末望水岸，入徑四寸。問︰井深幾何
術曰：置井徑五尺，以入徑四寸減之，餘，以乘立木五尺為實。以入徑四寸為法。實如法得一寸。
荅曰： a丈 。
"""

"""
Suppose there is a well with a diameter of 5 chi, but its depth is unknown.
A 5-chi-long pole is placed upright above the well. From the top of the pole, the edge of the water is observed, and the line of sight enters the diameter of the well by 4 cun.
Question: how deep is the well?

The procedure says: Place the well diameter of 5 chi, subtract the 4 cun of entry into the diameter, and the remainder is used.
Multiply this remainder by the upright pole of 5 chi to obtain the dividend.
Use the 4 cun of entry into the diameter as the divisor.
Divide the dividend by the divisor to obtain the depth in chi.

The answer says: *a* zhang.
"""

# 井徑五尺
井徑 = 5

# 入徑四寸 (convert to chi: 1 chi = 10 cun)
入徑 = Fraction(4, 10)

# 立木五尺
立木 = 5

# 以井徑五尺減入徑四寸
餘 = 井徑 - 入徑

# 以餘乘立木五尺為實
實 = 餘 * 立木

# 以入徑四寸為法
法 = 入徑

# 實如法得井深 (in chi)
井深 = Fraction(實, 法)

# Convert depth to zhang (1 zhang = 10 chi)
a = 井深 / 10
"""
"""
