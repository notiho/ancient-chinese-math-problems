"""
今有五十八人二十九日食麫九十五斛三㪷一升少半升問人食幾何
術曰置麫斛斗升數為實以人日食相乘為法實如法得一
答曰 a升
"""

#----- content starts here -----
"""
Suppose there are 58 people eating for 29 days, consuming 95 hu, 3 dou, 1 sheng, and half a sheng of flour.
Question: how much flour does each person eat per day?

The procedure says: Place the number of hu, dou, and sheng of flour as the dividend.
Multiply the number of people and the number of days as the divisor.
Divide the dividend by the divisor, obtaining the amount of flour each person eats per day.

Answer: *a* sheng.
"""

# 置麫斛斗升數為實
# Convert 95 hu, 3 dou, 1 sheng, and half a sheng into sheng
# 1 hu = 10 dou, 1 dou = 10 sheng
麫 = (95 * 10 * 10) + (3 * 10) + 1 + Fraction(1, 2)

# 以人日食相乘為法
人數 = 58
日數 = 29
法 = 人數 * 日數

# 實如法得一
a = Fraction(麫, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 17/3, Actual: 19063/3364"""
