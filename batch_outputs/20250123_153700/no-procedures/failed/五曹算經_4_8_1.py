"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
答曰： a斛 奇 b分 。
"""

"""
Suppose there is a pile of millet on flat ground. The base circumference is 3 zhang, and the height is 4 chi.
Question: how much millet is there?

Answer: *a* hu and *b* fen.
"""

# 下周三丈 (base circumference)
base_circumference = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高四尺 (height)
height = 4  # in chi

# Formula for the volume of a cone: V = (1/3) * base_area * height
# Base area (A) = (circumference^2) / (4 * π), but in ancient Chinese math, π is approximated as 3.
base_area = (base_circumference ** 2) / (4 * 3)

# Volume of the cone (V)
volume = Fraction(1, 3) * base_area * height

# Convert volume from cubic chi to hu
# 1 hu = 10 cubic chi
a = volume // 10  # Whole hu
b = volume % 10  # Remaining fen (1 fen = 1 cubic chi)

a, b  # Output the result as a hu and b fen
"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 10.0
Variable 'b' has wrong value. Expected: 34/25, Actual: 0.0"""
