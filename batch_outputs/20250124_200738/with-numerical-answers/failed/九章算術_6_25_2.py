"""
今有池，五渠注之。其一渠開之，少半日一滿；次，一日一滿；次，二日半一滿；次，三日一滿；次，五日一滿。今皆決之，問︰幾何日滿池？
術曰：各置渠一日滿池之數，并以為法。以一日為實。實如法得一日。
荅曰： a(=15/74)日 。
"""

#----- content starts here -----
"""
Suppose there is a pool filled by five channels. 
The first channel alone fills the pool in half a day, the second in one day, the third in two and a half days, the fourth in three days, and the fifth in five days.
Now, if all the channels are opened together, how many days will it take to fill the pool?

The procedure says: Place the amount of the pool filled by each channel in one day. Add these together to form the divisor.
Take one day as the dividend.
Divide the dividend by the divisor to obtain the number of days to fill the pool.

Answer: *a*(=15/74) days.
"""

# 各置渠一日滿池之數
渠1 = Fraction(1, Fraction(1, 2))  # First channel fills 1 pool in 1/2 day -> fills 2 pools in 1 day
渠2 = Fraction(1, 1)               # Second channel fills 1 pool in 1 day -> fills 1 pool in 1 day
渠3 = Fraction(1, 2 + Fraction(1, 2))  # Third channel fills 1 pool in 2.5 days -> fills 2/5 pools in 1 day
渠4 = Fraction(1, 3)               # Fourth channel fills 1 pool in 3 days -> fills 1/3 pools in 1 day
渠5 = Fraction(1, 5)               # Fifth channel fills 1 pool in 5 days -> fills 1/5 pools in 1 day

# 并以為法
法 = 渠1 + 渠2 + 渠3 + 渠4 + 渠5

# 以一日為實
實 = 1

# 實如法得一日
a = Fraction(實, 法)  # 15/74 days#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15/74, Actual: 15/59"""
