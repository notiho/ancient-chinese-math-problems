"""
今有甲發長安，五日至齊；乙發齊，七日至長安。今乙發已先二日，甲乃發長安。問︰幾何日相逢？
術曰：并五日、七日以為法。以乙先發二日減七日，餘，以乘甲日數為實。實如法得一日。
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose person A departs from Chang'an and takes 5 days to reach Qi.
Person B departs from Qi and takes 7 days to reach Chang'an.
Now, person B departs 2 days earlier than person A. 
Question: after how many days will they meet?

The procedure says: Combine the 5 days and 7 days as the divisor.
Subtract the 2 days that B departs earlier from the 7 days, obtaining the remainder.
Multiply this remainder by the number of days A travels, obtaining the dividend.
Divide the dividend by the divisor to find the number of days until they meet.

Answer: *a* days.
"""

from fractions import Fraction

# 甲發長安，五日至齊
甲日數 = 5

# 乙發齊，七日至長安
乙日數 = 7

# 乙發已先二日
乙先發 = 2

# 并五日、七日以為法
法 = 甲日數 + 乙日數

# 以乙先發二日減七日，餘
餘 = 乙日數 - 乙先發

# 以乘甲日數為實
實 = 餘 * 甲日數

# 實如法得一日
a = Fraction(實, 法)

a#----- content ends here -----

"""
"""
