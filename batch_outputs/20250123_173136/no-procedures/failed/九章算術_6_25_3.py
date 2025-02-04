"""
今有池，五渠注之。其一渠開之，少半日一滿；次，一日一滿；次，二日半一滿；次，三日一滿；次，五日一滿。今皆決之，問︰幾何日滿池？
荅曰： a日 。
"""

"""
Suppose there is a pool being filled by five channels of water. The filling rates of the channels are as follows:
- The first channel fills the pool in half a day.
- The second channel fills the pool in 1 day.
- The third channel fills the pool in 2.5 days.
- The fourth channel fills the pool in 3 days.
- The fifth channel fills the pool in 5 days.

If all channels are opened simultaneously, how many days will it take to fill the pool?

Answer: *a* days.
"""

from fractions import Fraction

# Filling rates of each channel (in pools per day)
rate1 = Fraction(1, 0.5)  # First channel fills in half a day
rate2 = Fraction(1, 1)    # Second channel fills in 1 day
rate3 = Fraction(1, 2.5)  # Third channel fills in 2.5 days
rate4 = Fraction(1, 3)    # Fourth channel fills in 3 days
rate5 = Fraction(1, 5)    # Fifth channel fills in 5 days

# Total rate when all channels are opened
total_rate = rate1 + rate2 + rate3 + rate4 + rate5

# Time to fill the pool (1 pool divided by total rate)
a = Fraction(1, total_rate)

# Result
a
"""
Code error: both arguments should be Rational instances"""
