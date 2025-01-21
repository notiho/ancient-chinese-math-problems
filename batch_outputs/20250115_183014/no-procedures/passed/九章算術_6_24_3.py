"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
荅曰： a畝 。
"""

"""
Suppose there is a farming task. One person can plow 7 mu in one day, another can till 3 mu in one day, and another can sow 5 mu in one day.
Now, if one person is tasked to plow, till, and sow all by themselves in one day, how much land can they manage?

Answer: *a* mu.
"""

# 一人一日發七畝
plowing_rate = Fraction(7)

# 一人一日耕三畝
tilling_rate = Fraction(3)

# 一人一日耰種五畝
sowing_rate = Fraction(5)

# Calculate the combined rate (since one person must do all tasks in one day)
combined_rate = 1 / (1 / plowing_rate + 1 / tilling_rate + 1 / sowing_rate)

# The amount of land managed in one day is the combined rate
a = combined_rate
"""
"""
