"""
今有七人九日造成弓十二張半今有十七人造弓十五張問幾何日訖
術曰置今造弓數以弓日數乘之又以成弓人數乘之為實以今有人數乘本有弓數為法實如法得一
答曰 a日
"""

"""
Suppose 7 people in 9 days can make 12.5 bows. 
Now, there are 17 people making 15 bows.
Question: how many days will it take?

The procedure says: Place the current number of bows to be made.
Multiply it by the number of bow-days, and also multiply it by the number of people who completed the bows, obtaining the dividend.
Multiply the current number of people by the original number of bows, obtaining the divisor.
Divide the dividend by the divisor, obtaining the number of days.

Answer: *a* days.
"""

# 本有七人
本有人數 = 7

# 九日
本有日數 = 9

# 造成弓十二張半
本有弓數 = Fraction(25, 2)

# 今有十七人
今有人數 = 17

# 造弓十五張
今造弓數 = 15

# 以弓日數乘之
弓日數 = 本有日數 * 本有弓數

# 又以成弓人數乘之，為實
實 = 弓日數 * 本有人數

# 以今有人數乘本有弓數，為法
法 = 今有人數 * 今造弓數

# 實如法得一
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 378/85, Actual: 105/34"""
