"""
今有程耕，一人一日發七畝，一人一日耕三畝，一人一日耰種五畝。今令一人一日自發、耕、耰種之，問︰治田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there are three tasks in farming:
1. Plowing (fa): one person can plow 7 mu in one day.
2. Tilling (geng): one person can till 3 mu in one day.
3. Sowing (youzhong): one person can sow 5 mu in one day.

Now, if one person is required to complete all three tasks (plowing, tilling, and sowing) in one day, how much land can they manage?

Answer: *a* mu.
"""

# Plowing rate (fa): 7 mu/day
plowing_rate = Fraction(1, 7)

# Tilling rate (geng): 3 mu/day
tilling_rate = Fraction(1, 3)

# Sowing rate (youzhong): 5 mu/day
sowing_rate = Fraction(1, 5)

# Total rate of completing all tasks in one day
total_rate = plowing_rate + tilling_rate + sowing_rate

# Total land managed in one day
a = Fraction(1, total_rate)  # Inverse of the total rate to get the land managed

a#----- content ends here -----

"""
"""
