"""
今有圓窖，下周二百八十六尺，深三丈六尺。問：受粟幾何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a circular pit with a circumference of 286 chi at the bottom and a depth of 3 zhang and 6 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu of millet.
"""

# 下周 (circumference) = 286 chi
下周 = 286

# 深 (depth) = 3 zhang 6 chi = 36 chi
深 = 3 * 10 + 6

# 圓窖的底面積 (Area of the circular base) = (circumference^2) / (4 * pi)
# Using an approximation of pi = 3 for simplicity in ancient Chinese math
底面積 = Fraction(下周**2, 4 * 3)

# 圓窖的體積 (Volume of the pit) = 底面積 * 深
體積 = 底面積 * 深

# 粟的體積換算 (Convert volume to hu): 1 hu = 10 cubic chi
a = Fraction(體積, 10)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4089800/27, Actual: 122694/5"""
