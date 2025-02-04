"""
今有委米依垣內角，下周八尺，高五尺。問︰積及為米幾何？
荅曰：積 a尺 。為米 b斛 ， c斛 。
"""

"""
Suppose there is a pile of rice stacked against the inner corner of a wall. The base circumference is 8 chi, and the height is 5 chi.
Question: what is the volume of the pile, and how much rice does it represent?

Answer: the volume is *a* cubic chi, and the rice is *b* hu and *c* dou.
"""

# 下周八尺 (base circumference)
base_circumference = 8

# 高五尺 (height)
height = 5

# The base area of the pile is a quarter-circle (πr^2 / 4).
# From the circumference, we calculate the radius (r = circumference / (2π)).
# Then, the volume is (1/4) * π * r^2 * height.

# Using π ≈ 3 for simplicity (as was often done in ancient Chinese calculations):
pi = 3
radius = Fraction(base_circumference, 2 * pi)
base_area = Fraction(1, 4) * pi * radius**2
volume = base_area * height

# Convert the volume into rice (1 cubic chi = 1 hu of rice).
# 1 hu = 10 dou.
a = volume  # Volume in cubic chi
b = int(volume)  # Whole hu
c = (volume - b) * 10  # Remaining dou

# Final results:
a = Fraction(a)
b = Fraction(b)
c = Fraction(c)
"""
Variable 'a' has wrong value. Expected: 320/9, Actual: 20/3
Variable 'b' has wrong value. Expected: 21, Actual: 6
Variable 'c' has wrong value. Expected: 691/729, Actual: 20/3"""
