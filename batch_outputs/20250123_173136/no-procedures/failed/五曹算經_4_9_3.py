"""
今有內角聚粟下周五十四尺高五尺。問：粟㡬何？
答曰： a斛 。
"""

"""
Suppose there is a granary with a square base, where the perimeter of the base is 54 chi, and the height is 5 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu.
"""

# 下周 (perimeter of the base) = 54 尺
下周 = 54

# 高 (height) = 5 尺
高 = 5

# Calculate the side length of the square base
邊長 = 下周 / 4

# Calculate the area of the base (square area = side^2)
底面積 = 邊長 * 邊長

# Calculate the volume of the granary (volume = base area * height)
體積 = 底面積 * 高

# Convert volume in cubic chi to hu (1 hu = 10 cubic chi)
a = Fraction(體積, 10)
"""
Code error: both arguments should be Rational instances"""
