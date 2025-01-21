"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
荅曰： a畝 。
"""

"""
Suppose there is a farming task. One person can plow 7 mu in one day, another can till 3 mu in one day, and another can sow seeds for 5 mu in one day. 
Now, if one person is tasked to do all three tasks (plowing, tilling, and sowing) in one day, how much land can they manage?

Answer: *a* mu.
"""

# 一人一日發七畝
plowing_rate = 7

# 一人一日耕三畝
tilling_rate = 3

# 一人一日耰種五畝
sowing_rate = 5

# The total rate is determined by the slowest task (since all tasks must be completed for the same piece of land)
a = Fraction(1, Fraction(1, plowing_rate) + Fraction(1, tilling_rate) + Fraction(1, sowing_rate))
"""
"""
