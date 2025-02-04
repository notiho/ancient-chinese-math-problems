"""
今有平地聚粟，下周三丈六尺，高四尺五寸。問：粟幾何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground. The base circumference is 3 zhang 6 chi, and the height is 4 chi 5 cun.
Question: how much millet is there?

Answer: *a* hu.
"""

# 下周三丈六尺 (base circumference)
周 = 3 * 10 + 6  # Convert zhang and chi to chi (1 zhang = 10 chi)

# 高四尺五寸 (height)
高 = 4 + Fraction(5, 10)  # Convert chi and cun to chi (1 chi = 10 cun)

# Formula for the volume of a cone: V = (周 / 2π)^2 * 高 / 3
# π is approximated as 3 in ancient Chinese math
π = 3
半徑 = Fraction(周, 2 * π)  # 半徑 = 周 / (2π)
體積 = (半徑 ** 2) * 高 / 3  # Volume in cubic chi

# Convert cubic chi to hu (1 hu = 10 cubic chi)
a = 體積 / 10#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 100, Actual: 27/5"""
