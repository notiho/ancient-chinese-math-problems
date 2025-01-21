"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
答曰： a斛 奇 b分 。
"""

"""
Suppose there is a pile of millet on flat ground. The base circumference is 3 zhang, and the height is 4 chi.
Question: how much millet is there?

Answer: *a* hu and *b* fen.
"""

# 下周三丈 (base circumference is 3 zhang)
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高四尺 (height is 4 chi)
高 = 4

# Formula for the volume of a cone: V = (1/3) * base_area * height
# Base area = (周 / 2π)^2 * π = (周^2) / (4π)
# Volume = (1/3) * (周^2) / (4π) * 高 = (周^2 * 高) / (12π)

# Using π ≈ 3 for simplicity (as was common in ancient Chinese calculations)
π = 3
體積 = Fraction(周**2 * 高, 12 * π)

# Convert volume to hu (1 hu = 10 chi^3)
a = 體積 // 10  # Whole hu
b = 體積 % 10  # Remaining fen (1 fen = 1 chi^3)

a, b  # Final result in hu and fen
"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 10
Variable 'b' has wrong value. Expected: 34/25, Actual: 0"""
