"""
今有池，五渠注之。其一渠開之，少半日一滿；次，一日一滿；次，二日半一滿；次，三日一滿；次，五日一滿。今皆決之，問︰幾何日滿池？
術曰：各置渠一日滿池之數，并以為法。以一日為實。實如法得一日。
荅曰： a(=15/74)日 。
"""

#----- content starts here -----
"""
Suppose there is a pool, and five channels flow into it.
The first channel, when opened, fills the pool in half a day.
The second channel fills it in one day.
The third channel fills it in two and a half days.
The fourth channel fills it in three days.
The fifth channel fills it in five days.
Now, if all channels are opened together, question: how many days does it take to fill the pool?

The procedure says: Place the amount of the pool each channel fills in one day, and sum them to obtain the divisor.
Take one day as the dividend.
Divide the dividend by the divisor to obtain the number of days.

The answer says: *a*(=15/74) days.
"""

from fractions import Fraction

# 各置渠一日滿池之數
渠1 = Fraction(1, Fraction(1, 2))  # First channel fills in 1/0.5 = 2 pools per day
渠2 = Fraction(1, 1)               # Second channel fills in 1 pool per day
渠3 = Fraction(1, 2.5)             # Third channel fills in 1/2.5 pools per day
渠4 = Fraction(1, 3)               # Fourth channel fills in 1/3 pools per day
渠5 = Fraction(1, 5)               # Fifth channel fills in 1/5 pools per day

# 并以為法
法 = 渠1 + 渠2 + 渠3 + 渠4 + 渠5

# 以一日為實
實 = 1

# 實如法得一日
a = Fraction(實, 法)  # 15/74 days#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
