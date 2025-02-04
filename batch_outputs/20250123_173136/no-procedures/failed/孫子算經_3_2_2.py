"""
今有平地聚粟，下周三丈六尺，高四尺五寸。問：粟幾何？
答曰： a斛 。
"""

"""
Suppose there is a flat ground where millet is piled. The base circumference is 3 zhang 6 chi, and the height is 4 chi 5 cun.
Question: how much millet is there?

Answer: *a* hu.
"""

# 下周三丈六尺 (base circumference)
下周 = 3 * 10 + 6  # Convert zhang to chi (1 zhang = 10 chi)

# 高四尺五寸 (height)
高 = 4 + Fraction(5, 10)  # Convert cun to chi (1 chi = 10 cun)

# Formula for the volume of a cone: V = (C^2 * h) / (36 * π)
# Here, π is approximated as 3, as per ancient Chinese calculations.

# Volume in cubic chi
體積 = (下周 ** 2 * 高) / (36 * 3)

# Convert cubic chi to hu (1 hu = 10 cubic chi)
a = 體積 / 10
"""
Variable 'a' has wrong value. Expected: 100, Actual: 27/5"""
