"""
今有方窖，廣四丈六尺，長五丈四尺，深三丈五尺。問：受粟幾何？
答曰： a斛 。
"""

"""
Suppose there is a square cellar with:
- Width: 4 zhang 6 chi
- Length: 5 zhang 4 chi
- Depth: 3 zhang 5 chi

Question: How much millet can it hold?

Answer: *a* hu.
"""

# Convert dimensions to chi (1 zhang = 10 chi)
廣 = 4 * 10 + 6  # 4 zhang 6 chi
長 = 5 * 10 + 4  # 5 zhang 4 chi
深 = 3 * 10 + 5  # 3 zhang 5 chi

# Calculate the volume in cubic chi
體積 = 廣 * 長 * 深

# Convert cubic chi to hu (1 hu = 100 cubic chi)
a = Fraction(體積, 100)  # Volume in hu

a  # Output the result
"""
Variable 'a' has wrong value. Expected: 161000/3, Actual: 4347/5"""
