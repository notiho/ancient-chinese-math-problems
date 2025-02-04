"""
今有井徑五尺不知其深立五尺木於井上從木末望水岸入徑四寸問井深幾何
術曰置井徑五尺以入徑四寸減之餘以乘立木五尺為實以入徑四寸為法實如法得一寸
荅曰 a丈 
"""

"""
Suppose there is a well with a diameter of 5 chi, and its depth is unknown.
A 5-chi-long pole is placed upright above the well. From the tip of the pole, the line of sight to the water's edge enters the well's diameter by 4 cun.
Question: how deep is the well?

The procedure says: Place the well's diameter of 5 chi. Subtract the entered diameter of 4 cun.
Take the remainder and multiply it by the upright pole of 5 chi, obtaining the dividend.
Take the entered diameter of 4 cun as the divisor.
Divide the dividend by the divisor, obtaining 1 chi.

The answer says: *a* zhang.
"""

# 井徑五尺
井徑 = 5  # chi

# 入徑四寸
入徑 = Fraction(4, 10)  # Convert cun to chi (1 chi = 10 cun)

# 減之，餘
餘 = 井徑 - 入徑

# 立木五尺
立木 = 5  # chi

# 餘以乘立木五尺，為實
實 = 餘 * 立木

# 以入徑四寸為法
法 = 入徑

# 實如法得一寸
井深 = Fraction(實, 法)  # Result in chi

# Convert chi to zhang (1 zhang = 10 chi)
a = 井深 / 10  # zhang
"""
"""
