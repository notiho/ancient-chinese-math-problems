"""
今有方窖從一丈三尺廣六尺深一丈。問：受粟㡬何？
答曰： a斛 奇 b寸 。
"""

"""
Suppose there is a square pit with a length of 1 zhang 3 chi, a width of 6 chi, and a depth of 1 zhang.
Question: how much millet can it hold?

Answer: it holds *a* hu and *b* cun.
"""

# Dimensions of the pit
length = 1 * 10 + 3  # 1 zhang 3 chi = 13 chi
width = 6  # 6 chi
depth = 1 * 10  # 1 zhang = 10 chi

# Volume of the pit in cubic chi
volume = length * width * depth

# 1 hu = 10 cubic chi
a = volume // 10  # Number of hu
b = volume % 10  # Remaining cun

a, b  # Output the result as (a hu, b cun)
"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 78
Variable 'b' has wrong value. Expected: 39/5, Actual: 0"""
