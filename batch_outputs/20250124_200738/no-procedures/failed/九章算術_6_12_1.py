"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a slow walker who starts first and walks 10 li. A fast walker chases after them for 100 li, and the fast walker arrives 20 li ahead of the slow walker.
Question: how many li does the fast walker travel to catch up with the slow walker?

Answer: the fast walker travels *a* li.
"""

# Slow walker starts with a 10 li head start
slow_walker_start = 10

# Fast walker ends up 20 li ahead of the slow walker
fast_walker_ahead = 20

# Total distance the fast walker travels to catch up
a = slow_walker_start + fast_walker_ahead

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 30"""
