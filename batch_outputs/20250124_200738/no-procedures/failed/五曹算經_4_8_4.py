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

# 下周三丈 (base circumference is 3 zhang)
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高四尺 (height is 4 chi)
高 = 4

# Formula for the volume of a conical pile: V = (周^2 * 高) / (36 * pi)
# Note: In ancient Chinese math, pi is approximated as 3.

體積 = Fraction(周**2 * 高, 36 * 3)

# Convert volume to hu (1 hu = 10 chi^3)
a = 體積 // 10  # Integer part in hu
b = 體積 % 10  # Remainder in chi^3 (fen)

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 3
Variable 'b' has wrong value. Expected: 34/25, Actual: 10/3"""
