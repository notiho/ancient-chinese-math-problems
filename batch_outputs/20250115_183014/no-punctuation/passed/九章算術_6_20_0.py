"""
今有甲發長安五日至齊乙發齊七日至長安今乙發已先二日甲乃發長安問幾何日相逢
術曰并五日七日以為法以乙先發二日減七日餘以乘甲日數為實實如法得一日
荅曰 a日 
"""

"""
Suppose person A departs from Chang'an and takes 5 days to reach Qi, while person B departs from Qi and takes 7 days to reach Chang'an.
Now, person B departs 2 days earlier than person A.
Question: after how many days will they meet?

The procedure says: Combine the 5 days and 7 days as the divisor.
Subtract the 2 days that person B departed earlier from the 7 days, and use the remainder to multiply the days person A travels, obtaining the dividend.
Divide the dividend by the divisor to get the number of days until they meet.

The answer says: *a* days.
"""

# 甲發長安五日
甲日數 = 5

# 乙發齊七日
乙日數 = 7

# 乙發已先二日
乙先發 = 2

# 并五日七日以為法
法 = 甲日數 + 乙日數

# 以乙先發二日減七日
餘 = 乙日數 - 乙先發

# 餘以乘甲日數為實
實 = 餘 * 甲日數

# 實如法得一日
a = Fraction(實, 法)
"""
"""
