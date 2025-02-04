"""
今有池，五渠注之。其一渠開之，少半日一滿；次，一日一滿；次，二日半一滿；次，三日一滿；次，五日一滿。今皆決之，問︰幾何日滿池？
術曰：各置渠一日滿池之數，并以為法。以一日為實。實如法得一日。
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose there is a pool being filled by five channels.
The first channel alone fills the pool in half a day.
The second channel alone fills the pool in one day.
The third channel alone fills the pool in two and a half days.
The fourth channel alone fills the pool in three days.
The fifth channel alone fills the pool in five days.
Now, if all channels are opened together, how many days will it take to fill the pool?

The procedure says: For each channel, calculate how much of the pool it fills in one day.
Add these together to form the divisor.
Take 1 day as the dividend.
Divide the dividend by the divisor to find the number of days it takes to fill the pool.

Answer: *a* days.
"""

from fractions import Fraction

# Each channel's rate of filling the pool in one day
渠1 = Fraction(1, Fraction(1, 2))  # 1 pool in half a day = 2 pools in 1 day
渠2 = Fraction(1, 1)               # 1 pool in 1 day
渠3 = Fraction(1, 2.5)             # 1 pool in 2.5 days
渠4 = Fraction(1, 3)               # 1 pool in 3 days
渠5 = Fraction(1, 5)               # 1 pool in 5 days

# Add the rates of all channels to form the divisor
法 = 渠1 + 渠2 + 渠3 + 渠4 + 渠5

# Take 1 pool as the dividend
實 = 1

# Calculate the number of days to fill the pool
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
