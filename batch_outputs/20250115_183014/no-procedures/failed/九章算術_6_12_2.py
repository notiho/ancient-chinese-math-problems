"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
荅曰： a里 。
"""

"""
Suppose there is a slower traveler who starts first and walks 10 li. A faster traveler starts later and chases the slower traveler for 100 li. The faster traveler arrives 20 li ahead of the slower traveler.
Question: how many li does the faster traveler walk to catch up to the slower traveler?

Answer: *a* li.
"""

# 不善行者先行 10 里
slow_traveler_distance = 10

# 善行者追之一百里
fast_traveler_chase_distance = 100

# 善行者先至 20 里
fast_traveler_lead = 20

# The distance the faster traveler walks to catch up
a = slow_traveler_distance + fast_traveler_chase_distance - fast_traveler_lead
"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 90"""
