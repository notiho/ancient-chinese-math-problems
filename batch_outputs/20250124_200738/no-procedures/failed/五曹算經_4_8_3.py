"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground. The base circumference is 3 zhang, and the height is 4 chi.
Question: how much millet is there?

Answer: *a* hu and *b* fen.
"""

# 下周三丈 (base circumference = 3 zhang)
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高四尺 (height = 4 chi)
高 = 4

# Formula for the volume of a cone: V = (1/3) * base_area * height
# Base area = (周 / 2π)^2 * π = (周^2) / (4π)
# Volume = (1/3) * (周^2) / (4π) * 高

# Use π = 22/7 for approximation
π = Fraction(22, 7)

# Calculate the volume in cubic chi
體積 = Fraction(1, 3) * (周**2) / (4 * π) * 高

# 1 cubic chi = 1 hu (volume is directly in hu)
a = int(體積)  # Integer part in hu
b = 體積 - a  # Fractional part in fen (1 hu = 10 fen)

# Convert fractional part to fen
b = b * 10  # Convert to fen

a, b  # Final result in hu and fen#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 95
Variable 'b' has wrong value. Expected: 34/25, Actual: 50/11"""
