"""
今有甲發長安，五日至齊；乙發齊，七日至長安。今乙發已先二日，甲乃發長安。問︰幾何日相逢？
術曰：并五日、七日以為法。以乙先發二日減七日，餘，以乘甲日數為實。實如法得一日。
荅曰： a(=25/12)日 。
"""

"""
Suppose person A departs from Chang'an and takes 5 days to reach Qi. 
Person B departs from Qi and takes 7 days to reach Chang'an. 
Now, person B has already departed 2 days earlier, and then person A departs from Chang'an.
Question: after how many days will they meet?

The procedure says: Combine 5 days and 7 days to make the divisor. 
Use the 2 days that person B departed earlier to subtract from 7 days, leaving the remainder. 
Multiply this remainder by the number of days person A takes to travel, making the dividend. 
Divide the dividend by the divisor to obtain the number of days until they meet.

Answer: *a*(=25/12) days.
"""

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
a = Fraction(實, 法) # 25/12 days
"""
"""
