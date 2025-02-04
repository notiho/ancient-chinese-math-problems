"""
今有倉南北一丈五尺東西三丈五尺髙八尺問受粟幾何
術曰以東西南北丈尺相乗又以髙乗之得積尺以斛法除之即粟數
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there is a granary with dimensions: north-south 1 zhang 5 chi, east-west 3 zhang 5 chi, and height 8 chi.
Question: how much millet can it hold?

The procedure says: Multiply the east-west and north-south dimensions (in zhang and chi) with each other, then multiply by the height, obtaining the volume in cubic chi.
Divide this by the hu divisor to get the number of hu of millet.

Answer: *a* hu.
"""

# 南北一丈五尺
南北 = 1 * 10 + 5  # Convert to chi (1 zhang = 10 chi)

# 東西三丈五尺
東西 = 3 * 10 + 5  # Convert to chi

# 高八尺
高 = 8  # Already in chi

# 以東西南北丈尺相乗
底面積 = 東西 * 南北

# 又以高乗之，得積尺
積尺 = 底面積 * 高

# 斛法 (1 hu = 100 cubic chi)
斛法 = 100

# 以斛法除之，即粟數
a = Fraction(積尺, 斛法)  # Result in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 70000/27, Actual: 42"""
