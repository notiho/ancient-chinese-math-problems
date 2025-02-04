"""
今有半壁聚粟下周三十六尺高四尺五寸。問：粟㡬何？
答曰： a斛 。
"""

"""
Suppose there is a half-wall-shaped pile of millet, with a base circumference of 36 chi and a height of 4 chi and 5 cun.
Question: how much millet is there?

Answer: *a* hu.
"""

# 半壁聚粟下周三十六尺
周 = 36  # circumference in chi

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # height in chi (convert 5 cun to chi)

# 半壁 (half-wall shape) is essentially half of a cylinder.
# The formula for the volume of a cylinder is: V = π * r^2 * h
# For a half-cylinder, the volume is halved: V = (1/2) * π * r^2 * h

# First, calculate the radius from the circumference: 周 = 2 * π * r
π = Fraction(22, 7)  # approximate value of π
半周 = Fraction(周, 2 * π)  # radius

# Volume of the half-cylinder (in cubic chi)
體積 = Fraction(1, 2) * π * 半周**2 * 高

# Convert cubic chi to hu (1 cubic chi = 10 hu)
a = 體積 * 10
"""
Variable 'a' has wrong value. Expected: 200, Actual: 25515/11"""
