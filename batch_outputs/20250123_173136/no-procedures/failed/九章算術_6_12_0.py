"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
荅曰： a里 。
"""

"""
Suppose there is a slow walker who starts walking 10 li ahead. A fast walker chases them for 100 li and overtakes the slow walker by 20 li.
Question: how many li does the fast walker need to walk to catch up to the slow walker?

Answer: the fast walker needs *a* li to catch up.
"""

# Slow walker starts 10 li ahead
slow_walker_start = 10

# Fast walker overtakes by 20 li after walking 100 li
fast_walker_overtake = 20

# The relative distance between the two walkers when the fast walker overtakes
relative_distance = slow_walker_start + fast_walker_overtake

# The fast walker needs to walk the same distance as the slow walker to catch up
a = relative_distance

# Result
a
"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 30"""
