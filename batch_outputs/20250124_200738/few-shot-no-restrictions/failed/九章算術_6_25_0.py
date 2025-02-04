"""
今有池，五渠注之。其一渠開之，少半日一滿；次，一日一滿；次，二日半一滿；次，三日一滿；次，五日一滿。今皆決之，問︰幾何日滿池？
術曰：各置渠一日滿池之數，并以為法。以一日為實。實如法得一日。
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose there is a pool, and five channels pour water into it.
The first channel, when opened, fills the pool in half a day.
The second channel fills the pool in one day.
The third channel fills the pool in two and a half days.
The fourth channel fills the pool in three days.
The fifth channel fills the pool in five days.
Now, if all channels are opened together, how many days will it take to fill the pool?

The procedure says: Place the amount of the pool each channel can fill in one day, and sum them to form the divisor.
Take one day as the dividend.
Perform the division to find how many days it takes to fill the pool.

The answer says: *a* days.
"""

from fractions import Fraction

# Each channel's rate of filling the pool in one day
渠1 = Fraction(1, Fraction(1, 2))  # First channel fills in 0.5 days, so rate is 2 pools/day
渠2 = Fraction(1, 1)               # Second channel fills in 1 day, so rate is 1 pool/day
渠3 = Fraction(1, 2.5)             # Third channel fills in 2.5 days, so rate is 2/5 pools/day
渠4 = Fraction(1, 3)               # Fourth channel fills in 3 days, so rate is 1/3 pools/day
渠5 = Fraction(1, 5)               # Fifth channel fills in 5 days, so rate is 1/5 pools/day

# Sum the rates of all channels
總率 = 渠1 + 渠2 + 渠3 + 渠4 + 渠5

# Time to fill the pool when all channels are opened
a = Fraction(1, 總率)

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
