"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
荅曰： a里 。
"""

"""
Suppose there is a slow walker who starts walking first and covers 10 li. A fast walker then starts chasing the slow walker and travels 100 li. 
The fast walker arrives 20 li ahead of the slow walker. 

Question: How many li does the fast walker need to travel to catch up with the slow walker?

Answer: The fast walker needs to travel *a* li.
"""

# Slow walker starts with a 10-li head start
slow_walker_start = 10

# Fast walker travels 100 li and ends up 20 li ahead of the slow walker
fast_walker_travel = 100
fast_walker_ahead = 20

# The distance the slow walker travels during this time
slow_walker_travel = fast_walker_travel - fast_walker_ahead

# The total distance the fast walker needs to travel to catch up
a = slow_walker_start + slow_walker_travel

a
"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 90"""
