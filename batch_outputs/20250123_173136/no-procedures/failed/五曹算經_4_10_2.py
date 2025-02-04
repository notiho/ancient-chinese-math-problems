"""
今有半壁聚粟下周三十六尺高四尺五寸。問：粟㡬何？
答曰： a斛 。
"""

"""
Suppose there is a half-wall-shaped pile of millet with a circumference of 36 chi at the base and a height of 4 chi and 5 cun.
Question: how much millet does it contain?

Answer: it contains *a* hu.
"""

# 下周三十六尺 (circumference of the base)
周 = 36

# 高四尺五寸 (height is 4 chi and 5 cun; 1 chi = 10 cun)
高 = 4 + Fraction(5, 10)

# 半壁聚粟 (half-wall shape, which is a semicircular base)
# The formula for the volume of a semicircular prism is: (1/2) * π * r^2 * h
# Here, we approximate π as 3, and r (radius) is derived from the circumference: 周 = 2 * π * r

# Calculate the radius
π = 3
r = Fraction(周, 2 * π)

# Calculate the volume in cubic chi
體積 = Fraction(1, 2) * π * r**2 * 高

# Convert cubic chi to hu (1 hu = 10 cubic chi)
a = Fraction(體積, 10)
"""
Variable 'a' has wrong value. Expected: 200, Actual: 243/10"""
