"""
今有五十八人二十九日食麫九十五斛三㪷一升少半升問人食幾何
術曰置麫斛斗升數為實以人日食相乘為法實如法得一
答曰 a升
"""

"""
Suppose there are 58 people, and for 29 days they consume 95 hu, 3 dou, 1 sheng, and half a sheng of flour.
Question: how much does one person eat per day?

The procedure says: Place the number of hu, dou, and sheng of flour as the dividend.
Multiply the number of people and days together as the divisor.
Divide the dividend by the divisor to obtain the amount one person eats per day.

Answer: *a* sheng.
"""

# 置麫斛斗升數為實
# Convert 95 hu, 3 dou, 1 sheng, and half a sheng into sheng
hu_to_sheng = 10 * 10  # 1 hu = 10 dou, 1 dou = 10 sheng
dou_to_sheng = 10      # 1 dou = 10 sheng
sheng = 1              # 1 sheng
half_sheng = Fraction(1, 2)  # Half a sheng

實 = (95 * hu_to_sheng) + (3 * dou_to_sheng) + sheng + half_sheng

# 以人日食相乘為法
人數 = 58
日數 = 29
法 = 人數 * 日數

# 實如法得一
a = Fraction(實, 法)  # Amount one person eats per day in sheng
"""
Variable 'a' has wrong value. Expected: 17/3, Actual: 19063/3364"""
