"""
今有池五渠注之其一渠開之少半日一滿次一日一滿次二日半一滿次三日一滿次五日一滿今皆決之問幾何日滿池
術曰各置渠一日滿池之數并以為法以一日為實實如法得一日
荅曰 a日 
"""

#----- content starts here -----
"""
Suppose there is a pool being filled by five channels. 
The first channel fills the pool in half a day, the second in one day, the third in two and a half days, the fourth in three days, and the fifth in five days.
Now, if all channels are opened together, question: how many days does it take to fill the pool?

The procedure says: Place the numbers of days each channel takes to fill the pool in one day.
Add them together to form the divisor.
Take 1 day as the dividend.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a* days.
"""

# 各置渠一日滿池之數
渠1 = Fraction(1, Fraction(1, 2))  # First channel fills in 1/2 day
渠2 = Fraction(1, 1)               # Second channel fills in 1 day
渠3 = Fraction(1, 2 + Fraction(1, 2))  # Third channel fills in 2.5 days
渠4 = Fraction(1, 3)               # Fourth channel fills in 3 days
渠5 = Fraction(1, 5)               # Fifth channel fills in 5 days

# 并以為法
法 = 渠1 + 渠2 + 渠3 + 渠4 + 渠5

# 以一日為實
實 = 1

# 實如法得一日
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15/74, Actual: 15/59"""
