"""
今有丁九萬八千七百六十六凡二十五丁出一兵問兵幾何
術曰置丁九萬八千七百六十六為實以二十五為法實如法即得
答曰 a人 奇 b 丁
"""

"""
Suppose there are 98,766 ding (households). For every 25 ding, one soldier is recruited.
Question: how many soldiers are recruited, and how many ding are left over?

The procedure says: Place 98,766 ding as the dividend. Use 25 as the divisor.
Divide the dividend by the divisor to obtain the number of soldiers. The remainder is the leftover ding.

Answer: *a* soldiers, with *b* ding remaining.
"""

# 置丁九萬八千七百六十六為實
實 = 98766

# 以二十五為法
法 = 25

# 實如法即得
a = 實 // 法  # Number of soldiers
b = 實 % 法   # Remaining ding
"""
"""
