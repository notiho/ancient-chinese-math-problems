"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a farming task. One person can clear 7 mu in one day, one person can plow 3 mu in one day, and one person can harrow and sow 5 mu in one day.
Now, if one person is tasked to clear, plow, and harrow/sow the field in one day, how much land can they manage?

Answer: *a* mu.
"""

# Clearing rate per day
clearing_rate = Fraction(7)

# Plowing rate per day
plowing_rate = Fraction(3)

# Harrowing and sowing rate per day
harrowing_sowing_rate = Fraction(5)

# The total rate is determined by the slowest task
a = Fraction(1, (1 / clearing_rate + 1 / plowing_rate + 1 / harrowing_sowing_rate))#----- content ends here -----

"""
"""
