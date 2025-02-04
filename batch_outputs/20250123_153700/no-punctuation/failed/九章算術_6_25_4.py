"""
今有池五渠注之其一渠開之少半日一滿次一日一滿次二日半一滿次三日一滿次五日一滿今皆決之問幾何日滿池
術曰各置渠一日滿池之數并以為法以一日為實實如法得一日
荅曰 a日 
"""

"""
Suppose there is a pond being filled by five channels. 
The first channel fills the pond in half a day, the second in one day, the third in two and a half days, the fourth in three days, and the fifth in five days.
If all channels are opened together, how many days does it take to fill the pond?

The procedure says: Place the number of days each channel takes to fill the pond in one day. 
Add them together to form the divisor.
Take one day as the dividend.
Divide the dividend by the divisor to obtain the number of days.

The answer says: *a* days.
"""

# 各置渠一日滿池之數
渠1 = Fraction(1, Fraction(1, 2))  # First channel fills in half a day
渠2 = Fraction(1, 1)               # Second channel fills in one day
渠3 = Fraction(1, Fraction(5, 2))  # Third channel fills in two and a half days
渠4 = Fraction(1, 3)               # Fourth channel fills in three days
渠5 = Fraction(1, 5)               # Fifth channel fills in five days

# 并以為法
法 = 渠1 + 渠2 + 渠3 + 渠4 + 渠5

# 以一日為實
實 = 1

# 實如法得一日
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 15/74, Actual: 15/59"""
