"""
今有七人九日造成弓十二張半今有十七人造弓十五張問幾何日訖
術曰置今造弓數以弓日數乘之又以成弓人數乘之為實以今有人數乘本有弓數為法實如法得一
答曰 a日
"""

"""
Suppose there are 7 people who, in 9 days, make 12.5 bows. 
Now, there are 17 people who need to make 15 bows.
Question: how many days will it take?

The procedure says: Place the current number of bows to be made.
Multiply it by the number of bow-days.
Then multiply it by the number of people who completed the bows, obtaining the dividend.
Multiply the current number of people by the original number of bows, obtaining the divisor.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a* days.
"""

# 本有七人九日造成弓十二張半
本有人數 = 7
本有日數 = 9
本有弓數 = Fraction(25, 2)  # 12.5 bows

# 今有十七人造弓十五張
今有人數 = 17
今有弓數 = 15

# 置今造弓數
弓數 = 今有弓數

# 以弓日數乘之
弓日數 = 本有日數 * 本有弓數
實 = 弓數 * 弓日數

# 又以成弓人數乘之
實 *= 本有人數

# 以今有人數乘本有弓數為法
法 = 今有人數 * 本有弓數

# 實如法得一
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 378/85, Actual: 945/17"""
