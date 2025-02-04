"""
今有方窖，廣四丈六尺，長五丈四尺，深三丈五尺。問：受粟幾何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a square pit with a width of 4 zhang 6 chi, a length of 5 zhang 4 chi, and a depth of 3 zhang 5 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu.
"""

# Convert dimensions to chi (1 zhang = 10 chi)
廣 = 4 * 10 + 6  # 4 zhang 6 chi
長 = 5 * 10 + 4  # 5 zhang 4 chi
深 = 3 * 10 + 5  # 3 zhang 5 chi

# Calculate the volume in cubic chi
體積 = 廣 * 長 * 深

# 1 cubic chi holds 10 hu of millet
a = Fraction(體積 * 10)  # Convert to hu

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 161000/3, Actual: 869400"""
