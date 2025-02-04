"""
今有委粟平地，下周一十二丈，高二丈。問︰積及為粟幾何？
荅曰：積 a尺 。為粟 b斛 。
"""

"""
Suppose there is a pile of millet on flat ground, with a base circumference of 12 zhang and a height of 2 zhang.
Question: what is the volume of the pile, and how much millet does it contain?

Answer: the volume is *a* cubic chi, and the amount of millet is *b* hu.
"""

# 下周 (circumference) = 12 丈
下周 = 12 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高 (height) = 2 丈
高 = 2 * 10  # Convert zhang to chi

# Calculate the radius of the base
# Circumference = 2 * pi * radius -> radius = circumference / (2 * pi)
# Using an approximation for pi = 3
半徑 = 下周 / (2 * 3)

# Volume of a cone = (1/3) * pi * r^2 * h
積 = Fraction(1, 3) * 3 * 半徑**2 * 高  # Use pi ≈ 3

# Convert volume to millet
# 1 cubic chi = 1/10 hu
為粟 = 積 * Fraction(1, 10)

# Final results
a = 積  # Volume in cubic chi
b = 為粟  # Amount of millet in hu
"""
Variable 'b' has wrong value. Expected: 80000/27, Actual: 800.0"""
