"""
今有圓囷周三丈，高一丈六尺。問：受粟㡬何？
答曰： a斛 奇 b尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical granary with a circumference of 3 zhang and a height of 1 zhang 6 chi.
Question: how much grain can it hold?

Answer: it holds *a* hu and an additional *b* chi³.
"""

# 圓囷周三丈 (circumference = 3 zhang)
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈六尺 (height = 1 zhang 6 chi)
高 = 1 * 10 + 6  # Convert zhang and chi to chi

# Formula for the volume of a cylinder: V = π * r² * h
# Here, π is approximated as 3, and r = 周 / (2 * π)

π = 3
半徑 = 周 / (2 * π)

# Volume in cubic chi
體積 = π * 半徑**2 * 高

# Convert cubic chi to hu (1 hu = 1000 cubic chi)
a = int(體積 // 1000)  # Whole hu
b = 體積 % 1000  # Remaining cubic chi

a, b  # Output the result as (a hu, b chi³)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 740, Actual: 1
Variable 'b' has wrong value. Expected: 6/5, Actual: 200.0"""
