"""
今有方窖，廣四丈六尺，長五丈四尺，深三丈五尺。問：受粟幾何？
答曰： a斛 。
"""

"""
Suppose there is a square storage pit with:
- Width: 4 zhang 6 chi (4丈6尺)
- Length: 5 zhang 4 chi (5丈4尺)
- Depth: 3 zhang 5 chi (3丈5尺)

Question: How much millet can it hold?

Answer: It can hold *a* hu (斛).
"""

# Convert dimensions to chi (1 zhang = 10 chi)
width = 4 * 10 + 6  # 4丈6尺 = 46尺
length = 5 * 10 + 4  # 5丈4尺 = 54尺
depth = 3 * 10 + 5  # 3丈5尺 = 35尺

# Calculate the volume in cubic chi
volume_in_cubic_chi = width * length * depth

# Convert cubic chi to hu (1 hu = 100 cubic chi)
a = Fraction(volume_in_cubic_chi, 100)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 161000/3, Actual: 4347/5"""
