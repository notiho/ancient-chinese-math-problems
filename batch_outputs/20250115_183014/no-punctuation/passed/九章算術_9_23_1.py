"""
今有井徑五尺不知其深立五尺木於井上從木末望水岸入徑四寸問井深幾何
術曰置井徑五尺以入徑四寸減之餘以乘立木五尺為實以入徑四寸為法實如法得一寸
荅曰 a丈 
"""

"""
Suppose there is a well with a diameter of 5 chi. Its depth is unknown.
A 5-chi pole is placed upright above the well. From the top of the pole, the edge of the water is observed to be 4 cun inside the diameter of the well.
Question: how deep is the well?

The procedure says: Place the well's diameter of 5 chi, subtract the 4 cun of the inward diameter, and take the remainder.
Multiply this remainder by the upright pole's 5 chi to obtain the dividend.
Take the 4 cun of the inward diameter as the divisor.
Divide the dividend by the divisor to obtain the depth in chi.

The answer says: *a* zhang.
"""

# 井徑五尺
井徑 = 5

# 入徑四寸 (convert to chi: 1 chi = 10 cun)
入徑 = Fraction(4, 10)

# 立木五尺
立木 = 5

# 置井徑五尺，以入徑四寸減之
餘 = 井徑 - 入徑

# 餘以乘立木五尺，為實
實 = 餘 * 立木

# 以入徑四寸為法
法 = 入徑

# 實如法得一寸 (depth in chi)
井深 = Fraction(實, 法)

# Convert depth to zhang (1 zhang = 10 chi)
a = 井深 / 10
"""
"""
