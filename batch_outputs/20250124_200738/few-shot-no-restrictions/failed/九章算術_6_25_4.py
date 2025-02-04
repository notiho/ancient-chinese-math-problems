"""
今有池，五渠注之。其一渠開之，少半日一滿；次，一日一滿；次，二日半一滿；次，三日一滿；次，五日一滿。今皆決之，問︰幾何日滿池？
術曰：各置渠一日滿池之數，并以為法。以一日為實。實如法得一日。
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose there is a pond, and five channels flow into it. 
The first channel, when opened, fills the pond in half a day.
The second channel fills the pond in one day.
The third channel fills the pond in two and a half days.
The fourth channel fills the pond in three days.
The fifth channel fills the pond in five days.
If all channels are opened together, how many days will it take to fill the pond?

The procedure says: Place the amount of the pond filled in one day by each channel. Add these together to form the divisor. 
Take one day as the dividend. Divide the dividend by the divisor to find the number of days required to fill the pond.

Answer: *a* days.
"""

from fractions import Fraction

# Each channel's contribution to filling the pond in one day
渠1 = Fraction(1, Fraction(1, 2))  # First channel fills in 1/2 day, so 1/0.5 = 2 ponds/day
渠2 = Fraction(1, 1)              # Second channel fills in 1 day, so 1/1 = 1 pond/day
渠3 = Fraction(1, 2.5)            # Third channel fills in 2.5 days, so 1/2.5 = 2/5 ponds/day
渠4 = Fraction(1, 3)              # Fourth channel fills in 3 days, so 1/3 ponds/day
渠5 = Fraction(1, 5)              # Fifth channel fills in 5 days, so 1/5 ponds/day

# Add the contributions to form the divisor (法)
法 = 渠1 + 渠2 + 渠3 + 渠4 + 渠5

# Take one day as the dividend (實)
實 = 1

# Calculate the number of days required to fill the pond
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
