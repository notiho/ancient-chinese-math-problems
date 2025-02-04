"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
答曰： a斛 奇 b分 。
"""

"""
Suppose there is an external corner (a cone-like shape) filled with millet. The base circumference is 48 chi, and the height is 6 chi.
Question: how much millet does it contain?

Answer: *a* hu and *b* fen.
"""

# Base circumference
周 = 48

# Height
高 = 6

# The formula for the volume of a cone-like shape is:
# Volume = (Base Area * Height) / 3
# The base area of a circle is derived from the circumference: Area = (Circumference^2) / (4 * π)
# In ancient Chinese math, π is approximated as 3.

# Base area
底面積 = (周 ** 2) / (4 * 3)

# Volume
體積 = (底面積 * 高) / 3

# Convert volume from cubic chi to hu (1 hu = 10 cubic chi)
a = int(體積 // 10)  # Whole hu
b = Fraction(體積 % 10, 10)  # Remaining fraction in fen

a, b  # Final result in hu and fen
"""
Code error: both arguments should be Rational instances"""
