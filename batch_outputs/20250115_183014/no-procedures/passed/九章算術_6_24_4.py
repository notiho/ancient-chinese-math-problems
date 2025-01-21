"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
荅曰： a畝 。
"""

"""
Suppose there are three tasks for farming: plowing, tilling, and sowing. 
One person can plow 7 mu in one day, till 3 mu in one day, and sow 5 mu in one day.
If one person is required to complete all three tasks in one day, how much land can they manage?

Answer: *a* mu.
"""

# Plowing rate per day
plowing_rate = Fraction(1, 7)  # 1 mu requires 1/7 of a day to plow

# Tilling rate per day
tilling_rate = Fraction(1, 3)  # 1 mu requires 1/3 of a day to till

# Sowing rate per day
sowing_rate = Fraction(1, 5)  # 1 mu requires 1/5 of a day to sow

# Total time required for all tasks for 1 mu
time_per_mu = plowing_rate + tilling_rate + sowing_rate

# Amount of land managed in 1 day
a = Fraction(1, time_per_mu)  # Invert the time per mu to get mu per day

a
"""
"""
