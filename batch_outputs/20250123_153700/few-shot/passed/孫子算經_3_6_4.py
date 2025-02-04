"""
今有丁九萬八千七百六十六，凡二十五丁出一兵。問：兵幾何？
術曰：置丁九萬八千七百六十六為實，以二十五為法。實如法，即得。
答曰： a人 奇 b 丁。
"""

"""
Suppose there are 98,766 ding (adult males). For every 25 ding, one soldier is conscripted.
Question: how many soldiers are conscripted, and how many ding are left over?

The procedure says: Place 98,766 ding as the dividend. Use 25 as the divisor.
Divide the dividend by the divisor. The quotient is the number of soldiers, and the remainder is the leftover ding.

Answer: *a* soldiers and *b* ding.
"""

# 置丁九萬八千七百六十六為實
實 = 98766

# 以二十五為法
法 = 25

# 實如法，即得
a = 實 // 法  # Quotient: number of soldiers
b = 實 % 法   # Remainder: leftover ding
"""
"""
