"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
荅曰： a里 。
"""

"""
Suppose there is a slower traveler who starts by walking 10 li ahead. A faster traveler chases the slower one for 100 li and arrives 20 li ahead of the slower traveler.
Question: how many li does the faster traveler walk to catch up to the slower traveler?

Answer: *a* li.
"""

# 不善行者先行一十里
slower_start = 10

# 善行者追之一百里
faster_chase = 100

# 善行者先至不善行者二十里
faster_ahead = 20

# The distance the faster traveler walks to catch up
a = faster_chase - faster_ahead + slower_start
"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 90"""
