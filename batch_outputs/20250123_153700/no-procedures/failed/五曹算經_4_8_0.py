"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
答曰： a斛 奇 b分 。
"""

"""
Suppose there is a pile of millet on flat ground. The base circumference is 3 zhang, and the height is 4 chi.
Question: how much millet is there?

Answer: *a* hu and *b* fen.
"""

# 下周三丈 (base circumference = 3 zhang = 30 chi)
base_circumference = 30  # in chi

# 高四尺 (height = 4 chi)
height = 4  # in chi

# Formula for the volume of a cone: V = (1/3) * base_area * height
# Base area = (circumference^2) / (4 * π), but ancient Chinese math approximates π as 3
# So, base_area = (circumference^2) / 12

base_area = Fraction(base_circumference**2, 12)

# Volume of the cone
volume = Fraction(1, 3) * base_area * height

# 1 hu = 10 dou = 100 sheng, and 1 chi^3 = 1 sheng
# Convert the volume in chi^3 to hu and fen
a = volume // 100  # Number of hu
b = volume % 100  # Remaining fen (in sheng)

a, b  # Final result in hu and fen
"""
Variable 'a' has wrong value. Expected: 1543/25, Actual: 1
Variable 'b' has wrong value. Expected: 34/25, Actual: 0"""
